## [Brute Force Attack](https://owasp.org/www-community/attacks/Brute_force_attack)

This vulnerability is on the signin page: http://localhost:8080/index.php?page=signin.

The root password found in http://localhost:8080/whatever/htpasswd doesn't work.

We tried bruteforcing with `hydra` and `ffuz` but kept getting timeouts from the server. We ended up writing our own asynchronous bruteforce attacker for more control.

```console
$ python brute_force_attack/resources/parallel.py
[SUCCESS] Username: root | Password: shadow
[SUCCESS] Username: admin | Password: shadow
[SUCCESS] Username: user | Password: shadow
```

It looks like all users have at least the `shadow` password. Signing in with any combination gives the flag: `b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2`.

This vulnerability can be prevented with:

- A stronger password policy: minimum size, digits, lowercase, uppercase and special characters
- No backdoor password
- Limit the amount of password attempts with timeouts
