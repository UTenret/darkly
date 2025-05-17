## [Exposure of Information Through Directory Listing](https://cwe.mitre.org/data/definitions/548.html)

The http://localhost:8080/robots.txt file shows a `/.hidden` directory. In it, there are a lot of directories and subdirectories, each having a short README taunting us with messages such as `Try again`.

There are too many directories to explore manually so we wrote a crawler and we get:

```console
$ python exposure_of_information_through_directory_listing/resources/crawler.py
========================================
Found in http://localhost:8080/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README:
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
========================================
```

`robots.txt` is not a security measure, it is just a convention to prevent crawlers from looking at directories. This vulnerability can be prevented by having appropriate server configuration to restrict access to sensitive directories.

For example with `nginx`:

```
server {
    listen 80;
    server_name your-domain.com;

    root /var/www/your-site-root;

    # Block access to the .hidden directory
    location ~ /\.hidden {
        deny all;
        return 403;
    }

    # Disable directory listing globally
    location / {
        autoindex off;
    }
}
```
