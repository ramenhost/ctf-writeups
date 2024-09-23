## crypto/hard-to-implement
I have a flag for you. We should talk more over my secure communications channel.
`nc chal.competitivecyber.club 6001`  
**Given:** `cryptor.py`

## Remote service
The remote service running on `nc chal.competitivecyber.club 6001` is `cryptor.py`.

### cryptor.py
```python
#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from external import *
import socketserver, signal

listen = 1337
attempts = 1500
flag = getflag()

def encrypt(key,plaintext):
	cipher = AES.new(key, AES.MODE_ECB)
	pt = pad(plaintext + flag.encode(), 16)
	return cipher.encrypt(pt).hex()

def serve(req):
	key = get_random_bytes(16)
	tries = 0
	req.sendall(b"Thank you for using our secure communications channel.\nThis channel uses top-shelf military-grade encryption.\nIf you are not the intended recepient, you can't read our secret.")
	while tries < attempts:
		req.sendall(b'\n('+str.encode(str(tries))+b'/'+str.encode(str(attempts))+b') ')
		req.sendall(b'Send challenge > ')
		try:
			ct = encrypt(key, req.recv(4096).strip(b'\n'))
			req.sendall(b"Response > " + ct.encode() + b'\n')
		except Exception as e:
			req.sendall(b"An error occured!\n")
		tries += 1
	req.sendall(b'\nMax attempts exceeded, have a good day.\n')

class incoming(socketserver.BaseRequestHandler):
	def handle(self):
		signal.alarm(1500)
		req = self.request
		serve(req)

def main():
	socketserver.TCPServer.allow_reuse_address = True
	server = ReusableTCPServer(("0.0.0.0", listen), incoming)
	server.serve_forever()

if __name__ == "__main__":
	main()

```

## Solution
The remote service takes out input, appends flag and performs AES_ECB encryption. Since ECB mode does not use IV, same key and plaintext pair will output same ciphertext always.
AES block size is 16 bytes. By controlling our input length, we can control how many flag characters will be present in first block.

Let's assume flag to be `PCTF{UNKNOWN}`. The below table shows how AES first block changes with input length.

| Input              | Input + Flag (`AES first block`)| No of flag chars in first block |
|--------------------|---------------------------------|---------------------------------|
| AAAAAAAAAAAAAAA    | `AAAAAAAAAAAAAAAP`CTF{UNKNOWN}  |  1                              |
| AAAAAAAAAAAAAA     | `AAAAAAAAAAAAAAPC`TF{UNKNOWN}   |  2                              |

To brute force the first character of the flag, we can send input of length 15 `AAAAAAAAAAAAAAA` and consider the output's first block as truth ciphertext. 
```
Truth ciphertext = AES(key, `AAAAAAAAAAAAAAAP`)
```
We then send all possible characters in 16th position (`AAAAAAAAAAAAAAAA` `AAAAAAAAAAAAAAAB`, `AAAAAAAAAAAAAAAC`, ...). If the first block of any output is same as truth ciphertext, then we have found the first character of the flag.

Similarly, we can bruteforce the enitire flag by sending inputs of length 15, 14, 13, ... 1 and comparing the first block of ciphertext.

### solve.py
```python
from pwn import *
import string

host = 'chal.competitivecyber.club'
port = 6001

flag_charset = string.printable

flag = 'pctf{'
junk = 'A' * 16

def encrypt(conn, data):
    conn.sendlineafter(b'Send challenge > ', data.encode())
    conn.recvuntil(b'Response > ')
    return conn.recvline().strip()

conn = remote(host, port)

p = log.progress('Flag: ')

while flag[-1] != '}':
    payload = junk[:-(len(flag)+1)]
    truth = encrypt(conn, payload)[:32]
    for c in flag_charset:
        p.status(f'{flag}{c}')
        if truth == encrypt(conn, payload + flag + c)[:32]:
            flag += c
            break

p.success(flag)
conn.close()
```

## Flag
```bash
ramenhost@ctf$ python3 solve.py 
[+] Opening connection to chal.competitivecyber.club on port 6001: Done
[+] Flag: : pctf{ab8zf58}
[*] Closed connection to chal.competitivecyber.club port 6001
```