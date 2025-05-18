## Client-Side Validation Bypass

The survey page (http://localhost:8080/index.php?page=survey) features an HTML form with a <select> element for grading, restricted to values between 1 and 10. However, this client-side restriction can be bypassed by modifying the form values through client-side manipulation (e.g., using browser developer tools).

Since the server-side lacks proper validation (relying solely on client-side checks), an attacker can submit any value, including those beyond the expected range. This exposes the application to Improper Input Validation (CWE-20) and Client-Side Validation Bypass, both categorized under Broken Access Control (OWASP A01:2021).
