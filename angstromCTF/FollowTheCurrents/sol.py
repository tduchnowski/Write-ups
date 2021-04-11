import os
import zlib


def keystream(seed):
    key = seed
    index = 0
    while 1:
        index += 1
        if index >= len(key):
            key += zlib.crc32(key).to_bytes(4,'big')
        yield key[index]

decrypted = []
enc_file = './enc'
with open(enc_file, 'rb') as e:
    msg = e.read()

for i in range(0,2**16):
    decrypted = []
    s = i.to_bytes(2,'big')
    k = keystream(s)
    for j in msg:
        decrypted.append( j ^ next(k))
    decrypted_bytes = bytes(decrypted)
    if b'actf{' in decrypted_bytes:
        print(decrypted_bytes)
        quit()
