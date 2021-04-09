import re
from pwn import *

regex_pattern = '>>\s(.*)\n'
MOD = 691
host = 'crypto.2021.chall.actf.co'
port = 21601
vals = []
conn = remote(host, port)
conn.recv()
for i in range(691):
    conn.send(str(i) + '\n')
    response = conn.recv().decode()
    m = re.search(regex_pattern, response)
    if m:
        vals.append(m.group(1))
    else:
        quit()

print(vals)
with open('server_values.txt', 'w') as f:
    content = ' '.join(vals)
    f.write(content)

