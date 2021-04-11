Challenge: Follow The Currents

Description: We have a ciphertext (enc) and a source code (source.py). We have
to decrypt enc.

Solution:
In the source.py code we see the code for key generation:
```python
def keystream():
	key = os.urandom(2)
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
		yield key[index]
```
Although the first value of the key is random, the rest of it is based on
zlib.crc32 method which is a method used for computing checksums, so it's
deterministic. The first value of the key is a random number of only 2 bytes.
Because of that, it's easy to brute force and check for all 2<sup>16</sup>
possibilities and look for 'actf{' in a decoded text.
This reads:
```
x''R@\xc5\x05\xfb/9\xe7\x10\x13L\xc5\xd6\x19 minutes left before the ctf starts
so i have no idea what to put here other than the flag which is
actf{low_entropy_keystream}
```
