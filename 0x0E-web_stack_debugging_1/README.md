Debuggin web stack
The issue is with the file /etc/nginx/sites-available
I remove it and replace it with a copy of /etc/nginx/sites/enabled

I used a symbolic link to do so.
ln: makes a symbolic link
-s: makes it a symbolic link not hard
-f: deletes existing file and replaces it
