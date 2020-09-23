#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10 ** 7)

#import math
#import numpy as np
N, M = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(M)]

G = {i: [] for i in range(1, N + 1)}

for x, y in xy:
    G[x].append(y)

dp = [-1] * (N + 1)

def dfs(num):
    if dp[num] != -1:
        return dp[num]

    t = 0

    for g in G[num]:
        t = max(t, dfs(g) + 1)

    dp[num] = t
    return t

ans = 0
for i in range(1, N + 1):
    ans = max(ans, dfs(i))

print(ans)