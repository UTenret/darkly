Vulnerability name : Client-Side Validation Bypass or Improper Input Validation or Parameter Tampering

How to defend : Validate Server-Side

This is the first vulnerability we found and we have the possibility to cheat very easily on a survey hosted on the website.
The server assumes the values as being from 1 to 10, but you can send the request with a much higher grade.

http://localhost:<port>/?page=survey
Inspect option of Ben
Change value to 11 or a much higher value for example

The page then updates with the corresponding higher value, which means the validation is done client-side, which you should almost never do.
