## mobile/guitar

Have you ever wanted to play the guitar on your phone? Here's a free app, with all guitar strings included for free!  
**Given:** com.nahamcon2024.guitar.apk

## Solution

Static analysis of APK can be done using https://mobsf.live/

MobSF discovered a hardcoded string named `secret_string`.
![secret string](secret_string.png)

```
$ echo "VGhlIGZsYWcgaXM6IGZsYWd7NDZhZmQ0ZjhkMmNhNTk1YzA5ZTRhYTI5N2I4NGFjYzF9Lg==" | base64 -d
The flag is: flag{46afd4f8d2ca595c09e4aa297b84acc1}
```