## [Unvalidated Redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)

There is a bunch of redirect links at the bottom for social media, (e.g. http://localhost:8080/index.php?page=redirect&site=instagram)

By modifying the `site` parameter to an unauthorized value, such as http://localhost:8080/index.php?page=redirect&site=phishingscam.net, we get the flag.

Unvalidated Redirects occur when an application allows users to be redirected to external websites without proper validation or restrictions. This can be exploited by attackers to redirect users from a trusted source to a malicious website, most commonly as part of a phishing scam.

This can be prevented by:

- Implementing strict validation for redirect URLs, allowing only trusted domains.
- Using a whitelist of allowed redirect URLs.
- Providing clear user warnings for any external links.
