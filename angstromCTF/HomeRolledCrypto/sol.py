import re
from pwn import *

def my_encrypt(enc_0, enc_1, plaintext):
    print(plaintext)
    plain_bin = bin(int(plaintext,16))[2:].rjust(32* 8, '0' )
    enc_0 = bin(int(enc_0,16))[2:].rjust(16 * 8,'0')
    enc_1 = bin(int(enc_1,16))[2:].rjust(16 * 8,'0')
    mapping = [{'0':enc_0[i], '1':enc_1[i]} for i in range(8 * 16)] * 2
    e = ''
    for index,n in enumerate(plain_bin):
        e += mapping[index][n]
    e = hex(int(e, 2))
    return e[2:]


host = 'crypto.2021.chall.actf.co'
port = 21602

conn = remote(host, port)
print(conn.read())
conn.send("1\n")
print(conn.read())
conn.send("00000000000000000000000000000000\n")
enc_0 = conn.read().decode('utf-8')[:32]
print(enc_0)
conn.send("1\n")
print(conn.read())
conn.send("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF\n")
enc_1 = conn.read().decode('utf-8')[:32]
print(enc_1)

conn.send("2\n")
regex = 'Encrypt this: (.*)\n'
for i in range(10):
    to_encrypt = conn.read().decode('utf-8')
    m = re.search(regex, to_encrypt)
    if m:
        to_encrypt = m.groups(1)[0]
    else:
        quit()
    conn.send(my_encrypt(enc_0, enc_1, to_encrypt) + '\n')

print(conn.read())


