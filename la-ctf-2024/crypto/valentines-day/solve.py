import itertools

with open("intro.txt") as f:
    pt = f.read()

with open("ct.txt") as f:
    ct = f.readlines()[0]

key = []
for p, c in zip(pt, ct):
    if p.isalpha():
        key.append((ord(c) - ord(p)) % 26) 

key.extend([0]*(161 - len(key)))

with open("ct.txt") as f:
    ct = f.read()

pt = ""
k = 0
c = 0
key_iter = itertools.cycle(key)
while c < len(ct):
    if ct[c].isalpha() and ct[c].isupper():
        pt += chr(((ord(ct[c]) - ord('A') - key_iter.__next__()) % 26) + ord('A'))
        k += 1
    elif ct[c].isalpha() and ct[c].islower():
        pt += chr(((ord(ct[c]) - ord('a') - key_iter.__next__()) % 26) + ord('a'))
        k += 1
    else:
        pt += ct[c]
    c += 1

print(pt[840:888])
