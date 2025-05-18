## [Stored XSS](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting.html)

This flag is broken. Writing `a` on both the `name` and `message` field is enough to get the flag.

Common vulnerabilities on comment fields are:

- Stored XSS: A user posts a comment like `<script>alert('Hacked');</script>`, which is executed when another user views the comment.
- SQL Injection: A user submits a comment containing `' OR '1'='1` which can manipulate database queries.
- HTML Injection: A comment like <iframe src="http://malicious-site.com"></iframe> can allow any third-party code to run on the client.

All these vulnerabilities can be prevented by proper input sanitization.
