from Crypto.Util.number import long_to_bytes
from math import gcd
from pwn import *

conn = remote("chall.lac.tf", 31171)
ct = int(conn.recvline().split()[-1])
N = int(conn.recvline().split()[-1])
e = int(conn.recvline().split()[-1])

pa_minus_qb = 0
qb_minus_pa = 0
while 1:
    conn.recvuntil(b"> ")
    conn.sendline(b"1")
    t = int(conn.recvline())
    if t != 1 and t != N -1:
        if pa_minus_qb == 0:
            pa_minus_qb = t
        else:
            qb_minus_pa = t
            break
    
# Try to calculate both as one becomes relatively prime to N (gcd 1)
pa = (((pa_minus_qb+1)//2) % N)
qb = (((qb_minus_pa+1)//2) % N)

p = gcd(pa, N)
q = gcd(qb, N)

# Drop the gcd 1 and take the other
p = q if p == 1 else p

q = N // p
phi_N = (p - 1) * (q - 1)
d = pow(e, -1, int(phi_N))

pt = pow(ct, d, N)
print(long_to_bytes(pt).decode())