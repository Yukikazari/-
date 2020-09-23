#!/usr/bin/env python3

#import
#import math
#import numpy as np
H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

def mod(num):
    return num % (10 ** 9 + 7)
    
dp = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            dp[i][j] = 1
            continue

        if A[i][j] == "#":
            continue

        if i == 0:
            dp[i][j] = dp[i][j - 1]
        elif j == 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = mod(dp[i - 1][j] + dp[i][j - 1])
            
print(dp[-1][-1])
