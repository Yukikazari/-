#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
X, Y = map(int, input().split())

# if X >= Y:
#     print(abs(Y - X))
#     exit()

t = 0
for i in range(1, 100):
    if X * (2 ** i) > Y:
        t = i - 1
        break

ans = 10 ** 20

for i in range(0, t + 3):
    x = abs(Y - X * (2 ** i))

    res = i
    
    res += x // (2 ** i)
    x %= (2 ** i)

    bx1 = bin(x)[2:]
    bx2 = bin(2 ** i - x)[2:]
    # print(bx)
    res += min(bx1.count("1"), bx2.count("1") + 1)

    ans = min(ans, res)

print(ans)