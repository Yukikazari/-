#import
#import math
#import numpy as np
#= int(input())
#= input()
N, W = map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]

x = [list(map(int, input().split())) for _ in range(N)]

dp = [[10**10] * (10 ** 5 + 10) for _ in range(N + 1)]

dp[0][0] = 0

#  i:N個目 j:価値

for i, (w, v) in enumerate(x, 1):
    for j in range(10**5 + 1):
        dp[i][j] = dp[i - 1][j]
        if j != 0 and v <= j:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - v] + w)

for i in range(10 ** 5, -1, -1):
    if dp[-1][i] <= W:
        print(i)
        exit()
