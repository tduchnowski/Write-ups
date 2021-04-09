from sage.all import *


def generate_eqs_matrix(n):
    mat = []
    for i in range(n):
        mat.append([ pow(i, n-j-1, MOD) for j in range(n) ])

    return matrix(GF(MOD),mat)

def check():
    for i in range(10, 400):
        eqs = generate_eqs_matrix(i)
        y = matrix(GF(MOD),vals[0:i]).transpose()
        solution = eqs.solve_right(y)
        solution = [chr(s[0]) for s in solution]
        solution = ''.join(solution)
        if 'actf{' in solution:
            print('FLAG FOUND')
            print(solution)
            quit()

        
MOD = 691
with open('server_values.txt', 'r') as f:
    vals = f.read().split(' ')
    vals = list(map(int, vals))

check()
