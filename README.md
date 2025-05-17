# darkly

Port forwarding: Guest 80 → Host 8080

A PHP website is now live on `localhost:8080`.

## gobuster commands

```console
$ git clone git@github.com:3ndG4me/KaliLists.git
```

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
[+] Extensions:              gif,jpg,jpeg,png
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/404.jpg              (Status: 200) [Size: 27027]
/42.jpeg              (Status: 200) [Size: 9783]
/banner2.jpg          (Status: 200) [Size: 50867]
/banner.jpg           (Status: 200) [Size: 511270]
/mailbox.png          (Status: 200) [Size: 49480]
/marvin.jpg           (Status: 200) [Size: 111300]
/search.png           (Status: 200) [Size: 49089]
/upload.png           (Status: 200) [Size: 64785]
/whoami.gif           (Status: 200) [Size: 1809804]
/win.png              (Status: 200) [Size: 72726]
/win.jpg              (Status: 200) [Size: 43468]
Progress: 102345 / 102350 (100.00%)
===============================================================
Finished
===============================================================
```
