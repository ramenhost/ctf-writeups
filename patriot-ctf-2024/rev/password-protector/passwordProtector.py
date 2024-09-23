# https://github.com/zrax/pycdc
# Apply patches: https://github.com/zrax/pycdc/issues/516 and https://github.com/zrax/pycdc/pull/472/files

# Source Generated with Decompyle++
# File: passwordProtector.pyc (Python 3.11)

import os
import secrets
from base64 import *

def promptGen():
    
    flipFlops = lambda x: chr(ord(x) + 1)
    with open('topsneaky.txt', 'rb') as f:
        first = f.read()
        None(None, None)
    with None:
        with None:
            if not None:
                pass
    bittys = secrets.token_bytes(len(first))
    onePointFive = int.from_bytes(first) ^ int.from_bytes(bittys)
    second = onePointFive.to_bytes(len(first))
    third = b64encode(second).decode('utf-8')
    bittysEnc = b64encode(bittys).decode('utf-8')
    fourth = ''
    for each in third:
        fourth += flipFlops(each)
        fifth = f'''Mwahahaha you will n{fourth[0:10]}ever crack into my pass{fourth[10:]}word, i\'ll even give you the key and the executable:::: {bittysEnc}'''
        return fifth


def main():
    print(promptGen())

if __name__ == '__main__':
    main()
