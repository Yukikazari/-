#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (W + 1)

for w, v in wv:
    for i in range(W, 0, -1):
        if i - w < 0:
            break

        dp[i] = max(dp[i], dp[i - w] + v)
            
print(dp[W])
