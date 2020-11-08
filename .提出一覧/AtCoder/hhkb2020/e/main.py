#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 10 ** 9 + 7

num = [1] * 400001

for i in range(1, 400001):
    num[i] = (num[i - 1] * 2) % MOD

ans = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        t = 1
        for k in range(i - 1, -1, -1):
            if S[k][j] == ".":
                t += 1
            else:
                break
        for k in range(i + 1, H):
            if S[k][j] == ".":
                t += 1
            else:
                break
        for k in range(j - 1, -1, -1):
            if S[i][k] == ".":
                t += 1
            else:
                break
        for k in range(j + 1, W):
            if S[i][k] == ".":
                t += 1
            else:
                break

        ans = (ans + t * num[t - 1]) % MOD

print(ans)