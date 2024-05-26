## scripting/base_3200

You know what to do.  
**Given:** theflag.xz

## Solution

We need to repeatedly base64 decode the contents until we get the flag.

```python
import base64

def decode_until_flag(file_path):
    with open(file_path, 'r') as file:
        encoded_str = file.read()
        
    while True:
        decoded_str = base64.b64decode(encoded_str).decode('utf-8')
        if decoded_str.startswith('flag'):
            return decoded_str
        else:
            encoded_str = decoded_str

file_path = 'theflag'
print(decode_until_flag(file_path))
```