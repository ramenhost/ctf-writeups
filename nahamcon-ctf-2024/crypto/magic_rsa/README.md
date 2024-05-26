## crypto/magic_rsa

Here's an RSA challenge using the most magical number of all.  
**Given:** output.txt, rsa_with_a_magic_number.py

## Solution

The script applied textbook RSA to each character in flag individually. The ASCII of each character is a tiny number compared to 2048-bit modulus N. This along with small public exponent, e, satisfies below condition where RSA will not work.
```
m^e < N
```

Hence, we can ignore the modulus and perform reverse of the modulus.

```python
ct = [1061208, 1259712, 912673, 1092727, 1860867, 175616, 166375, 941192, 185193, 1030301, 941192, 185193, 912673, 140608, 175616, 185193, 140608, 941192, 970299, 1061208, 175616, 912673, 117649, 912673, 185193, 148877, 912673, 125000, 110592, 1030301, 132651, 132651, 1061208, 117649, 117649, 1061208, 166375, 1953125]

flag = ""
for c in ct:
    flag += chr(round(pow(c, 1/3)))

print(flag)
```