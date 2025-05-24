## [Insecure Direct Object Reference](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References)

On the password recovery page http://localhost:8080/index.php?page=recover, the submit button sends a mail to webmaster@borntosec.com.

We can inspect, change the mail to whatever we want and submit, giving the flag: 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0

IDOR is now categorized under `Broken Access Control` in the OWASP Top Ten 2021 list. It can be mitigated by fetching the mail from the server-side user session data, instead of from user-submitted data.
