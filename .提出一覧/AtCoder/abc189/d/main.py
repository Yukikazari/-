#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
S = [input() for _ in range(N)]

ans = 1

c = 0

for i in range(N - 1, -1, -1):
    if S[i] == "AND":
        c += 1
    else:
        if c > 0:
            ans *= 2 ** c - 1
        c = 0

if c > 0:
    ans *= 2 ** (c + 1) - 1

print(2 ** (N + 1) - ans)