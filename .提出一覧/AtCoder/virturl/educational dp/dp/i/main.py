#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
P = list(map(float, input().split()))

# dp[i][j] : i枚投げてj枚表が出る確率
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i, p in enumerate(P, 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] * (1 - p)

        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] * p
        else:
            dp[i][j] = dp[i - 1][j] * (1 - p) + dp[i - 1][j - 1] * p

ans = 0
for i in range(N // 2 + 1, N + 1):
    ans += dp[-1][i]

print(ans)