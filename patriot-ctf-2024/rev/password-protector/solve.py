import base64

fourth = 'Ocmu{9gtuf' + 'MmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp'
bittysEnc = 'Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV'

bittys = base64.b64decode(bittysEnc)
flipFlops_inv = lambda x: chr(ord(x) - 1)
third = ''
for each in fourth:
    third += flipFlops_inv(each)
second = base64.b64decode(third)
onePointFive = int.from_bytes(second, 'big') ^ int.from_bytes(bittys, 'big')
print(onePointFive.to_bytes(len(second), 'big').decode())
