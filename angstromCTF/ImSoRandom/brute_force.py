import time
from pwn import *
from sympy.ntheory import factorint


def guess_next(s1, s2):
    print(s1,s2)
    DIGITS = 8
    s1 = int(str(s1**2).rjust(DIGITS*2, "0")[DIGITS//2:DIGITS + DIGITS//2])
    s2 = int(str(s2**2).rjust(DIGITS*2, "0")[DIGITS//2:DIGITS + DIGITS//2])
    return s1 * s2

def check(n):
    factorization = factorint(n)
    print(factorization)
    # not gonna work if any of the factors is < 10
    if [x for x in factorization.keys() if x < 10]: return None
    # look for primes which have 8 digits
    good_p = [x for x in factorization.keys() if len(str(x)) == 8]
    if not good_p: return None
    first_p = good_p[0]
    second_p = 1
    for p in factorization.keys():
        if p != first_p:
            second_p *= pow(p, factorization[p])
    return first_p, second_p

val = '609858911058389'
#val = sys.argv[1]
nums = check(int(val))
print(guess_next(nums[0], nums[1]))
#quit()
DIGITS = 8
while True:
    # connection to the server
    conn = remote('crypto.2021.chall.actf.co', 21600)
    for i in range(0,3):
        line = conn.recv()
        print(line)
        conn.send('r\n')
        line = int(conn.recvline().decode('utf-8'))
        print(line)
        nums = check(line)
        if nums:
            s1,s2 = nums[0], nums[1]
            guess = guess_next(s1,s2)
            print(guess)
            conn.send('g\n')
            print(conn.recv())
            conn.send(str(guess) + '\n')
            print(conn.recv())
            s1 = int(str(s1**2).rjust(DIGITS*2, "0")[DIGITS//2:DIGITS + DIGITS//2])
            s2 = int(str(s2**2).rjust(DIGITS*2, "0")[DIGITS//2:DIGITS + DIGITS//2])
            s1 = int(str(s1**2).rjust(DIGITS*2, "0")[DIGITS//2:DIGITS + DIGITS//2])
            s2 = int(str(s2**2).rjust(DIGITS*2, "0")[DIGITS//2:DIGITS + DIGITS//2])
            conn.send(str(s1 * s2) + '\n')
            print(conn.recv())
            time.sleep(5)
            quit()

        
    conn.close()
    time.sleep(5)
    

        
