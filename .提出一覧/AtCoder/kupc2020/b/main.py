#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, K = map(int, input().split())
V = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * K for _ in range(N)]

for i in range(K):
    dp[0][i] = 1

for i in range(1, N):
    cnt = -1
    sm = 0
    for j in range(K):
        t = V[i][j]
        while cnt < K - 1:
            if V[i - 1][cnt + 1] > t:
                break
            cnt += 1
            sm += dp[i - 1][cnt]
        if cnt >= 0:
            dp[i][j] = (dp[i][j] + sm) % (10 ** 9 + 7)

ans = sum(dp[N - 1]) % (10 ** 9 + 7)

print(ans)