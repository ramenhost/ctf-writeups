import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import itertools

# class copied from puzzle-room.py
class AESCipher(object):
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[: AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return AESCipher._unpad(cipher.decrypt(enc[AES.block_size :])).decode("utf-8")

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[: -ord(s[len(s) - 1 :])]

# all words from puzzle-room.py grid variable
wordlist = ["SPHINX","urn","vulture","arch","snake","urn","bug","plant","arch","staff","SPHINX","plant","foot","bug","plant",
            "vulture","foot","staff","vulture","plant","foot","bug","arch","staff","urn","Shrine","Shrine","Shrine","plant",
            "bug","staff","urn","arch","snake","vulture","foot","Shrine","Shrine","Shrine","urn","snake","vulture","foot","vulture",
            "staff","urn","bug","Shrine","Shrine","Shrine","foot","staff","bug","snake","staff","snake","plant","bug","urn","foot",
            "vulture","bug","urn","arch","foot","urn","SPHINX","arch","staff","plant","snake","staff","bug","plant","vulture","snake","SPHINX",
]

wordlist = set(wordlist) # history cannot have tiles with same name
wordlist.remove("Shrine") # end
wordlist.remove("SPHINX") # corners not allowed
wordlist.remove("vulture") # start

# enc_flag from puzzle-room.py try_get_tile()
enc_flag = b"FFxxg1OK5sykNlpDI+YF2cqF/tDem3LuWEZRR1bKmfVwzHsOkm+0O4wDxaM8MGFxUsiR7QOv/p904UiSBgyVkhD126VNlNqc8zNjSxgoOgs="

# we start at "vulture" and end at "Shrine". Brute force tiles in-between
# 4 or more steps needs to reach Shrine
for n in range(4, len(wordlist) + 1):
    for perm in itertools.permutations(wordlist, n):
        brute = ''.join(perm)
        key = "vulture" + brute + "Shrine"
        obj = AESCipher(key)
        try:
            dec_flag = obj.decrypt(enc_flag)
            if "pctf" in dec_flag:
                print(dec_flag)
                exit(0)
        except Exception:
            continue