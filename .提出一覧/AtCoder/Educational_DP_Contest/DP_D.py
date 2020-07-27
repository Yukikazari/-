#import
#import math
#import numpy as np
#= int(input())
#= input()
N, W = map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]

x = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, W + 1):
        dp[i][j] = dp[i - 1][j]
        if i != 0 and x[i - 1][0] <= j:
            dp[i][j] = max(dp[i][j], dp[i-1][j-x[i-1][0]] + x[i-1][1])

print(dp[-1][W])
