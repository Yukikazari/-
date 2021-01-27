#!/usr/bin/env python3

# from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)
#import math
#import numpy as np
N, M = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]

dp = [-10 ** 10] * N
g = {i:[] for i in range(N)}

for xy in XY:
    x, y = xy
    x -= 1; y -= 1
    g[x].append(y)

seen = [False] * N

def dfs(num):
    # print(num, seen)
    if seen[num]:
        return dp[num]

    seen[num] = True

    t = -10 ** 10

    for nextnum in g[num]:
        if not seen[nextnum]:
            dfs(nextnum)

        t = max(t, A[nextnum] - A[num], A[nextnum] - A[num] + dp[nextnum])

    dp[num] = max(dp[num], t)
    return dp[num]

ans = -10 ** 10

for i in range(N):
    if not seen[i]:
        ans = max(ans, dfs(i))
        

print(max(dp))
# print(dp)