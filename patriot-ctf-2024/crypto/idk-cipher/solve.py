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
