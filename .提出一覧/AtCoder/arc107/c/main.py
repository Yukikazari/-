#!/usr/bin/env python3

from atcoder.dsu import DSU
#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

t1 = DSU(N)
t2 = DSU(N)

for i in range(N):
    for j in range(i + 1, N):
        isok = True        
        for k in range(N):
            if A[i][k] + A[j][k] > K:
                isok = False
                break

        if isok:
            t1.merge(i, j)

for i in range(N):
    for j in range(i + 1, N):
        isok = True        
        for k in range(N):
            if A[k][i] + A[k][j] > K:
                isok = False
                break

        if isok:
            t2.merge(i, j)

a1 = 1
a2 = 1
t1l = t1.groups()
t2l = t2.groups()

dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    dp[i] = dp[i - 1] * i
    dp[i] %= 998244353

for t in t1l:
    a1 *= dp[len(t)]
    a1 %= 998244353
for t in t2l:
    a2 *= dp[len(t)]
    a2 %= 998244353

print(a1 * a2 % 998244353)