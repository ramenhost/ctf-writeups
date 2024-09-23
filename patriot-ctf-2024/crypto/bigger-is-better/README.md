## crypto/bigger-is-better
I heard choosing a small value for e when creating an RSA key pair is a bad idea. So I switched it up!  
**Given:** `dist.txt`

## Solution
When RSA public exponent (`e`) is large, private exponent tends to be small. Small `d` can be found using wiener's attack. I used `owiener` python module.

```python
#!/usr/bin/env python3
import owiener
from Crypto.Util.number import long_to_bytes

# copy values from dist.txt

N = 0xa0d9f4 ...
e = 0x5af5db ...
c = 0x731ceb ...

#--------Wiener's attack--------#

d = owiener.attack(e, N)

if d:
    m = pow(c, d, N)
    flag = long_to_bytes(m).decode()
    print(flag)
else:
    print("Wiener's Attack failed.")
```

## Flag
```bash
ramenhost@ctf$ python3 solve.py 
pctf{fun_w1th_l4tt1c3s_f039ab9}
```
