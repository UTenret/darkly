## [Improper Authentification](https://cwe.mitre.org/data/definitions/287.html)

On every page, there is a cookie `I_am_admin` = `68934a3e9455fa72420237eb05902327`.

The [dcode cipher identifier](https://www.dcode.fr/cipher-identifier) shows that the value is likely MD5, and the [MD5 decoder](https://www.dcode.fr/md5-hash) finds that it encodes `false`.

We then try to change the value to the MD5 hash of `true`

```console
$ echo -n 'true' | md5sum
b326b5062b2f0e69046810717534cb09  -
```

Lo and behold, an alert pops up with the flag: `Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3`

This vulnerability has several causes:

- Weak authentification mechanism: the use of a client-side cookie (`I_am_admin`) to determine user roles is inherently insecure. The server trusts client-provided data without proper verification.
- Predictable hashing algorithm: using MD5, a known weak hashing algorithm, for sensitive data such as authentication states. MD5 is vulnerable to hash collision and brute-force attacks.
- Security through obscurity: the application expects users not to understand the admin authentification, but once the process is understood it is trivial to exploit.
