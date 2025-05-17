## [Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)

Clicking on "© BornToSec" at the bottom of the index page leads us to an about page with a weird URL: http://localhost:8080/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f.

The `page` query argument is a sha256 encoded string, which we couldn't decrypt it through bruteforce attack

Looking at the source code reveals two hints.

```
[...]
You must come from : "https://www.nsa.gov/".
[...]
Let's use this browser : "ft_bornToSec". It will help you a lot.
[...]
```

The first comment is a reference to the referer, an optinal HTTP header field that identifies the address of the web page (i.e., the URI or IRI) from which the resource has been requested. (HTTP_referer)[https://en.wikipedia.org/wiki/HTTP_referer]

The second one is a reference to the user agent, a header indicating the browser which made the request.

We can craft the request with `curl`:

```console
$ curl 'http://localhost:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' -H 'User-Agent: ft_bornToSec' -H 'Referer: https://www.nsa.gov/' | grep flag
[...]
The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
[...]
```

Authentification through HTTP headers is a form of broken access control, since it is easily bypassed. Use a robust authentication mechanism (e.g., OAuth, JWT, or session-based authentication) instead of relying on HTTP headers for access control. Ensure that every request is authenticated and authorized on the server before processing.
