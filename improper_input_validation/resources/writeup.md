## [Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)

The survey page (http://localhost:8080/index.php?page=survey) features an HTML form with a `<select>` element for grading, restricted to values between 1 and 10.

We can update inspect the element and put a much bigger number in the `value` field. No validation is done server-side and we get the flag: 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa

This can be mitigated by doing the `value` validation server-side. The client should only ever be a representation of what is possible, with as little logic as possible.
