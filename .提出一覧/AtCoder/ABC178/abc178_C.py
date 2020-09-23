#import
#import math
#import numpy as np
modnum = 10 ** 9 + 7
N = int(input())

def mod(num):
    return num % modnum

def pow_k(x, n):
    if n == 0:
        return 1

    k = 1
    while n > 1:
        if n % 2 != 0:
            k *= x
        x = mod(x * x)
        n //= 2

    return mod(k * x)

t1 = pow_k(10, N)
t2 = pow_k(9, N)
t3 = pow_k(8, N)

print(mod(t1 - t3 - (t2 - t3) * 2))
