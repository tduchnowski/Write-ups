Challenge: Home Rolled Crypto

Description: Once again the give us a source for encryption algorithm. The
server gives us two options: either we can encrypt our own plaintext and they
respond with an encryption, or they give us plaintext and we have to encrypt it.
We have to match their encryption ten times in a row to get the flag.

Solution:
Let's have a look at the algorithm:
```python
class Cipher:
    BLOCK_SIZE = 16
    ROUNDS = 3
    def __init__(self, key):
        assert(len(key) == self.BLOCK_SIZE*self.ROUNDS)
        self.key = key

    def __block_encrypt(self, block):
        enc = int.from_bytes(block, "big")
        for i in range(self.ROUNDS):
            k = int.from_bytes(self.key[i*self.BLOCK_SIZE:(i+1)*self.BLOCK_SIZE], "big")
            enc &= k
            enc ^= k
        return hex(enc)[2:].rjust(self.BLOCK_SIZE*2, "0")


    def __pad(self, msg):
        if len(msg) % self.BLOCK_SIZE != 0:
            return msg + (bytes([0]) * (self.BLOCK_SIZE - (len(msg) % self.BLOCK_SIZE)))
        else:
            return msg

    def encrypt(self, msg):
        m = self.__pad(msg)
        e = ""
        for i in range(0, len(m), self.BLOCK_SIZE):
            e += self.__block_encrypt(m[i:i+self.BLOCK_SIZE])
        return e.encode()
```
Essentially, it takes our message, takes first block of length 16 bytes, then it
sends this block to another method "block_encrypt". This method, in turn,
divides the key in three parts, each 16 byte long. So it looks like this for the
first block.
```
PLAINTEXT: B1 B2 B3...
KEY:       K1 K2 K3

ALG:
1. (B1 & K1) ^ K1 = B1'
2. (B1' & K2) ^ K2 = B1''
3. (B1'' & K3) ^ K3 = First block of ciphertext
```
Then it does the same for second block, third block and so on.
So, if we have bit 1, which would be i-th bit in our plaintext, and we had
second plaintext which also have bit 1 in i-th position, they would have the
same i-th bits in their ciphertext. The same, of course, happens with bit 0.

To get the flag, we first send plaintext with all 0s, let it encrypt this
message, then do the same with all 1s (FFFFFF... in hex). Then we create a
mapping of how 0s and 1s behave in their places. Using this mapping we can
encrypt every message.

And the flag is:
```
actf{no_bit_shuffling_is_trivial}
```
