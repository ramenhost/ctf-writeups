## crypto/high-roller

We recieved word that a criminal APT had developed their own method for generating secure asymmetric encryption keys. We were able to intercept emails between the group including encrypted comms, and a 7zip file. All we managed to find in the 7zip file they sent out was their public key, and the key generator. Can you decrypt the comms?

**pycryptodome v3.20.0**

**Flag format:** CACI{}  
**Given:** `flag.enc`, `gen_setup.7z` (`notes.txt`, `BestEncrypt.py`, `public_key.pem`)

## Analysis

The script used by adversary is `BestEncrypt.py` which uses `pycryptodome` library to generate RSA keypair. 

### BestEncrypt.py
```python
#! /usr/bin/python3.10
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import random
import time

random.seed(int(time.time()))
p, q = getPrime(512, random.randbytes), getPrime(512, random.randbytes)
n = p*q
e = getPrime(512)
phi = (p-1)*(q-1)

assert GCD(e, phi) == 1
d = pow(e, -1, phi)

key = RSA.construct((n, e, d, p, q))
with open("public_key.pem", "wb") as f:
    f.write(key.publickey().export_key("PEM"))

with open("private_key.pem", "wb") as f:
    f.write(key.export_key("PEM"))
```

The public key is used to encrypt the flag and encrypted flag is stored in `flag.enc`.

## Solution

For RSA prime generation, the RNG is seeded with current time. If we can find the time at which the adversary generated the keypair, we can seed our RNG with that time and generate the same keypair. The given `gen_setup.7z` has preserved the time at which the keypair was generated. The `stat` command shows the last modified time of the public key file.
```bash
ramenhost@ctf$ stat -c '%n %y' public_key.pem 
public_key.pem 2024-09-21 22:39:18.000000000 +0530
```
We can convert the above datetime to unix timestamp and use it to seed our RNG. The following script generates the same RSA keypair as the adversary.

### solve.py
```python
import random
import subprocess
from Crypto.Util.number import *
from Crypto.PublicKey import RSA

# Unix timestamp of public_key.pem
key_timestamp = 1726938558

# taken from "openssl rsa -pubin -in public_key.pem -text -noout"
e = 0x00bd202092e27db343467c522563436c1ef2e51cee6cc0b02d728751011d954ad9c2fc485aa424e0162aa072360c8c40e8f6b4854b46bb9b07999697afc7da148b

random.seed(key_timestamp)
p, q = getPrime(512, random.randbytes), getPrime(512, random.randbytes)
n = p*q
phi = (p-1)*(q-1)

assert GCD(e, phi) == 1
d = pow(e, -1, phi)

key = RSA.construct((n, e, d, p, q))

with open("private_key.pem", "wb") as f:
    f.write(key.export_key("PEM"))

subprocess.run("openssl rsautl -decrypt -in flag.enc -inkey private_key.pem".split())
```

## Flag
```bash
ramenhost@ctf$ python3 solve.py 
CACI{T!ME_T0_S33D}
```