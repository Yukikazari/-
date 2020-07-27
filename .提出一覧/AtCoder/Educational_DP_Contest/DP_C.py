#import
#import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]

a = []

# dp[i][0]:Aを選んだ  dp[i][1]:Bを選んだ  dp[i][2]:Cを選んだ 

dp = [[0]*3 for _ in range(N+1)]

for _ in range(N):
    aa = list(map(int, input().split()))
    a.append(aa)

for i in range(1, N+1):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][k] = max(dp[i][k], dp[i-1][j]+a[i-1][k])

print(max(dp[-1]))