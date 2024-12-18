Vulnerability name: Unprotected / Unrestricted File Access

How to defend: Assume everything can be found and implement proper authentification. Again, use up to date hashing and a strong password policy.

So there is a file that every website is supposed to have called robots.txt.
This file indicates which directories the web-crawlers are supposed to not access.
It is at best a suggestion, as a malevolent crawler could easily ignore this file, and furthermore could use the information to attack the website.
Our website has a robots.txt file which looks like this :

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

In /whatever there is a htpasswd file containing

```
`root:437394baff5aa33daa618be47b75cb49`
```

We now have found what seems to be a hashed password for the user 'root'. It seems to be hashed in MD5, we crack the password using John the Ripper:

```bash
../john/run/john --format=Raw-MD5 htpasswd
```

And the output is :

```
Enabling duplicate candidate password suppressor
qwerty123@       (root)
```

So now we look for an entrypoint to the backend, which we find here :

http://localhost:8080/admin/

And using root as username and qwerty123@ as password enables us to login, giving us a flag.
