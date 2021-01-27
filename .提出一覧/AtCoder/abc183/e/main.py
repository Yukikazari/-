#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dp = [[0] * W for _ in range(H)]

Wsum = [0] * W
Dsum = [0] * ((H + W) * 2)

dp[0][0] = 1

for i in range(H):
    Hsum = 0
    for j in range(W):
        if S[i][j] == "#":
            Hsum = 0
            Wsum[j] = 0
            Dsum[j - i + W] = 0
            continue

        if i == j == 0:
            Hsum = dp[i][j]
            Wsum[j] = dp[i][j]
            Dsum[j - i + W] = dp[i][j]
            continue

        dp[i][j] += Wsum[j]
        dp[i][j] += Hsum
        dp[i][j] += Dsum[j - i + W]

        dp[i][j] %= (10 ** 9 + 7)

        Wsum[j] += dp[i][j]
        Hsum += dp[i][j]
        Dsum[j - i + W] += dp[i][j]

        Wsum[j] %= (10 ** 9 + 7)
        Hsum %= (10 ** 9 + 7)
        Dsum[j - i + W] %= (10 ** 9 + 7)


print(dp[-1][-1])
# print(Wsum)
# print(Dsum)