## crypto/idk-cipher
I spent a couple of hours with ???; now I am the world's best cryptographer!!! note: the flag contents will just random chars-- not english/leetspeak

**Cipher Text:** QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I=

Please wrap the flag with pctf{}.

**Given:** `encode.py`

## Analysis

The encryption script `encode.py` uses a custom cipher to encrypt the flag. It splits xor's first byte of key with both first and last byte of flag. Then, it xors the second byte of key with second and second last byte of flag and so on.

### encode.py
```python
import base64
# WARNING: This is a secret key. Do not expose it.
srt_key = 'secretkey' # // TODO: change the placeholder
usr_input = input("\t:"*10)
if len(usr_input) <= 1:
    raise ValueError("PT must be greater than 1")
if len(usr_input) % 2 != 0:
    raise ValueError("PT can only be an even number")
if not usr_input.isalnum():
    raise ValueError("Only alphabets and numbers supported")
# WARNING: Reversing input might expose sensitive information.
rsv_input = usr_input[::-1]
output_arr = []
for i in range(int(len(usr_input) / 2)):
    c1 = ord(usr_input[i])
    c2 = ord(rsv_input[i])
    enc_p1 = chr(c1 ^ ord(srt_key[i % len(srt_key)]))
    enc_p2 = chr(c2 ^ ord(srt_key[i % len(srt_key)]))
    output_arr.append(enc_p1)
    output_arr.append(enc_p2)
# WARNING: Encoded text should not be decoded without proper authorization.
encoded_val = ''.join(output_arr)
b64_enc_val = base64.b64encode(encoded_val.encode())
R = "R"*20
E = "E"*5
EXCLAMATION = "!"*5
print(f"ULTRA SUPE{R} SECUR{E} Encoded Cipher Text{EXCLAMATION}:", b64_enc_val.decode())
```

## Solution
Surprisingly, the key is hardcoded in the script. We can reverse the encryption process to get the flag.

```python
import base64

b64_enc_val = "QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I="
srt_key = 'secretkey'

# Calculate the srt_key from b64_enc_val
decoded_val = base64.b64decode(b64_enc_val)
first = bytearray()
second = bytearray()
key_len = len(srt_key)
for i in range(0, len(decoded_val), 2):
    byte1 = decoded_val[i]
    byte2 = decoded_val[i + 1] if i + 1 < len(decoded_val) else 0
    key_byte = ord(srt_key[(i // 2) % key_len])
    first.append(byte1 ^ key_byte)
    second.append(byte2 ^ key_byte)

print("pctf{" + first.decode() + bytearray(reversed(second)).decode() + "}")
```

## Flag
```bash
ramenhost@ctf$ python3 solve.py 
pctf{234c81cf3cd2a50d91d5cc1a1429855f}
```

