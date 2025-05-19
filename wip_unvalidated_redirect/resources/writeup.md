## [Unvalidated Redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)

There is a bunch of redirect links at the bottom for social media, (e.g. http://localhost:8080/index.php?page=redirect&site=instagram)

### Exploiting the Vulnerability

By modifying the `site` parameter to an unauthorized value, such as:

```
http://localhost:8080/index.php?page=redirect&site=ifoundavulnerability
```

This allows for unauthorized redirection, demonstrating the vulnerability.

---

Unvalidated Redirects occur when an application allows users to be redirected to external websites without proper validation or restrictions. This can be exploited by attackers to redirect users to malicious websites.

This can be prevented by:

- Implement strict validation for redirect URLs, allowing only trusted domains.
- Use a whitelist of allowed redirect URLs.
- Provide clear user warnings for any external links.
