Vulnerability name : Hidden Field Manipulation, Client-Side Validation Bypass

How to defend : Once again, no important validation logic should be in the front, hidden field are not a security measure

http://localhost:13080/index.php?page=recover
when asking to recover the password, the form has a hidden field

```
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

Change webmaster@borntosec.com to whatever
