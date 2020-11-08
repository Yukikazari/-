#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, M, K = map(int, input().split())
S = [list(map(int, input())) for _ in range(N)]

T = min(N, M)

ans = 0

for i in range(N):
    for j in range(M):
        cnt = {i:0 for i in range(10)}
        for k in range(min(T, N - i, M - j)):
            for a in range(k + 1):
                cnt[S[i + a][j + k]] += 1
            for a in range(k):
                cnt[S[i + k][j + a]] += 1

            if (k + 1) ** 2 - max(cnt.values()) <= K:
                ans = max(ans, k + 1)

print(ans)