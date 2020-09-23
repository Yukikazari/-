#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10 ** 9)
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

one = A.count(1)
two = A.count(2)
three = A.count(3)

dp = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

def calc(a, b, c):
    if dp[a][b][c] >= 0:
        return dp[a][b][c]

    if a + b + c == 0:
        return 0

    t = N

    if a > 0:
        t += calc(a - 1, b + 1, c) * a
    if b > 0:
        t += calc(a, b - 1, c + 1) * b
    if c > 0:
        t += calc(a, b, c - 1) * c
        
    t /= a + b + c

    dp[a][b][c] = t
    return t

ans = calc(three, two, one)
print(ans)
