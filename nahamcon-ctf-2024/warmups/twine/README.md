## warmups/twine

Google tells me that twine means: "strong thread or string consisting of two or more strands of hemp, cotton, or nylon twisted together."  
**Given:** twine.jpg

## Solution

`binwalk` shows two jpg images inside with size 34536 bytes each.
```bash
ramenhost@ctf:~/Git/ctf-writeups/nahamcon-ctf-2024/warmups/twinie$ binwalk twine.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
34574         0x870E          JPEG image data, JFIF standard 1.01
```

The filesize of twine.jpg is `(2 x 34536) + 38`. The 38 bytes sandwiched between two images is the flag.
```bash
head -c 34574 twine.jpg | tail -c 38
echo ""
```
