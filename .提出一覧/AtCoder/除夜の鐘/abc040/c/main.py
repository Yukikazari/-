#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

dp_max = 10 ** 9
dp = [dp_max] * N
dp[0] = 0

for i in range(1, N):
    dp[i] = min(dp[i - 1] + abs(A[i] - A[i - 1]), (dp[i - 2] + abs(A[i] - A[i - 2])) if i > 1 else dp_max)

print(dp[-1])