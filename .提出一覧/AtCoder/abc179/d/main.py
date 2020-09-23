#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
modnum = 998244353

N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]

def mod(num):
    return num % modnum

dp = [0] * (N + 1)
sdp = [0] * (N + 1)

dp[1] = 1
sdp[1] = 1

for i in range(2, N + 1):
    for l, r in LR:
        ri = max(0, i - l)
        li = max(0, i - r - 1)

        dp[i] += sdp[ri] - sdp[li]
        dp[i] = mod(dp[i])

    sdp[i] = sdp[i - 1] + dp[i]

print(dp[N])
