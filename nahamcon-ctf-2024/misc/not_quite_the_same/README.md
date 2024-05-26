## misc/not_quite_the_same

Everyone knows MD5 hashes. Everyone knows .png files! I believe you'll collide with greatness. 

Connect with:  
http://challenge.nahamcon.com:<port>

## Solution

The website lets us upload two png files. From challenge description, we can guess that the website uses MD5 hash to identify files. We need to create a MD5 collision to create an error in server.

I got two png files with same MD5 hash from  
- https://github.com/corkami/collisions/blob/master/examples/free/md5-s1.png
- https://github.com/corkami/collisions/blob/master/examples/free/md5-s2.png

Uploading these files to server, gives us the flag.