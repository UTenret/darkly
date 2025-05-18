# darkly

This project is meant as an introduction to web security.

Download `Darkly_i386.iso`, launch it and setup the port forwarding rule: Guest 80 → Host 8080. An insecure PHP website is now live on `localhost:8080`.

There are 14 flags to find:

- TODO: link1
- TODO: link2
- TODO: link...

## REDIRECTS

`index.php?page=redirect&site=http://evil.tld/phishing`

Unvalidated Redirects vs Open Redirects

## TODELETE GOBUSTER COMMANDS

```console
$ gobuster dir -u http://localhost:8080/ -w KaliLists/dirb/big.txt --exclude-length 975
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://localhost:8080/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                KaliLists/dirb/big.txt
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

```console
$ gobuster dir -u http://localhost:8080/images -w KaliLists/dirb/big.txt -x gif,jpg,jpeg,png --exclude-length 975
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://localhost:8080/images
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                KaliLists/dirb/big.txt
[+] Negative Status codes:   404
[+] Exclude Length:          975
[+] User Agent:              gobuster/3.6
[+] Extensions:              jpg,jpeg,png,gif
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/404.jpg              (Status: 200) [Size: 27027]
/42.jpeg              (Status: 200) [Size: 9783]
/banner.jpg           (Status: 200) [Size: 511270]
/banner2.jpg          (Status: 200) [Size: 50867]
/mailbox.png          (Status: 200) [Size: 49480]
/marvin.jpg           (Status: 200) [Size: 111300]
/search.png           (Status: 200) [Size: 49089]
/upload.png           (Status: 200) [Size: 64785]
/whoami.gif           (Status: 200) [Size: 1809804]
/win.jpg              (Status: 200) [Size: 43468]
/win.png              (Status: 200) [Size: 72726]
Progress: 102345 / 102350 (100.00%)
===============================================================
Finished
===============================================================
```

```console
ffuf -u http://localhost:8080/index.php\?page\=FUZZ -w KaliLists/dirb/big.txt -mc 200 -fs 0 -fr "Wtf"

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://localhost:8080/index.php?page=FUZZ
 :: Wordlist         : FUZZ: /media/axbrisse/ugreen/cursus/darkly/KaliLists/dirb/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200
 :: Filter           : Response size: 0
 :: Filter           : Regexp: Wtf
________________________________________________

default                 [Status: 200, Size: 6997, Words: 620, Lines: 134, Duration: 5ms]
feedback                [Status: 200, Size: 6596, Words: 387, Lines: 108, Duration: 8ms]
footer                  [Status: 200, Size: 1885, Words: 77, Lines: 55, Duration: 7ms]
header                  [Status: 200, Size: 3055, Words: 130, Lines: 87, Duration: 5ms]
media                   [Status: 200, Size: 1885, Words: 77, Lines: 55, Duration: 5ms]
member                  [Status: 200, Size: 2452, Words: 103, Lines: 72, Duration: 5ms]
recover                 [Status: 200, Size: 2396, Words: 98, Lines: 72, Duration: 5ms]
redirect                [Status: 200, Size: 1885, Words: 77, Lines: 55, Duration: 8ms]
signin                  [Status: 200, Size: 3006, Words: 124, Lines: 86, Duration: 5ms]
survey                  [Status: 200, Size: 5907, Words: 217, Lines: 212, Duration: 6ms]
upload                  [Status: 200, Size: 2489, Words: 107, Lines: 78, Duration: 6ms]
:: Progress: [20469/20469] :: Job [1/1] :: 6060 req/sec :: Duration: [0:00:03] :: Errors: 0 ::
```
