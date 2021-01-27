#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
H, W, K = map(int, input().split())
MOD = 998244353
dp = [[[0, H * W - K]] * W for _ in range(H)]
MAP = [[0] * W for _ in range(H)]

for _ in range(K):
    h, w, c = map(str, input().split())
    h = int(h); w = int(w)
    h -= 1; w -= 1

    if c == "R":
        MAP[h][w] = 1
    elif c == "D":
        MAP[h][w] = 2
    else:
        MAP[h][w] = 3

dp[0][0] = [1, H * W - K]

def calc(ix, iy, jx, jy):
    if iy == jy:
        pass

    elif iy > jy:
        ix *= pow(3, iy - jy, MOD)
        ix %= MOD
        iy = jy

    else:
        jx *= pow(3, jy - iy, MOD)
        jx %= MOD
        jy = iy

    return ix, iy, jx, jy

for i in range(H):
    for j in range(W):
        ix, iy = dp[i][j]

        if j < W - 1:
            a, b = dp[i][j + 1]
            if a != 0 and b != iy:
                ix, iy, a, b = calc(ix, iy, a, b)
            # print(a, b)

            if MAP[i][j] == 0:
                dp[i][j + 1] = [(a * 3 + ix * 2) % MOD, iy - 1]

            elif MAP[i][j] % 2 == 1:
                dp[i][j + 1] = [(a + ix) % MOD, iy]

        if i < H - 1:
            a, b = dp[i + 1][j]
            if a != 0 and b != iy:
                ix, iy, a, b = calc(ix, iy, a, b)
                # print(ix, iy, a, b)

            if MAP[i][j] == 0:
                dp[i + 1][j] = [(a * 3 + ix * 2) % MOD, iy - 1]

            elif MAP[i][j] // 2 == 1:
                dp[i + 1][j] = [(a + ix) % MOD, iy]

        # print(i, j, ix, iy, "000")
        # print(dp)

print(dp[-1][-1][0] * pow(3, dp[-1][-1][1]) % MOD)
# print(dp)