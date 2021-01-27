#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        if A[i - 1] == B[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

print(dp[-1][-1])

