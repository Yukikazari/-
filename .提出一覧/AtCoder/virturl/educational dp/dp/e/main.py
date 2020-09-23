#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [10 ** 10] * (10 ** 5 + 1)
dp[0] = 0

for w, v in wv:
    for i in range(10 ** 5, 0, -1):
        if i - v < 0:
            break

        dp[i] = min(dp[i], dp[i - v] + w)

for i in range(10 ** 5, 0, -1):
    if dp[i] <= W:
        print(i)
        exit()

