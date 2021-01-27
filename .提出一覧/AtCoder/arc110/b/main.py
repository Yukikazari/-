#!/usr/bin/env python3

#import
import math
#import numpy as np
N = int(input())
T = input()

s = "110" * (10 ** 5)

ans = 0

for i in range(3):
    isok = True
    for j in range(N):
        if T[j] != s[i + j]:
            isok = False
            break

    if isok:
        ans += 10 ** 10 - math.ceil((N + i - 3) / 3)

print(ans)