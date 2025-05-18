Vulnerability name: Unvalidated Redirects

How to defend: Prevent user being redirected to any website or you can add a disclaimer anytime the user clicks on an external link

There is a bunch of redirect links at the bottom to twitter, instagram and so on

```
http://localhost:8080/index.php?page=redirect&site=instagram
```

Modifying the site parameter to anything else that shouldnt be allowed gives us the flag

```
http://localhost:8080/index.php?page=redirect&site=ifoundavulnerability
```
