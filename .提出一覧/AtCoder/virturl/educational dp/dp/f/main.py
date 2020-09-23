#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = input()
T = input()

ls = len(S)
lt = len(T)

dp = [[0] * (lt + 1) for _ in range(ls + 1)]

for i in range(1, ls + 1):
    for j in range(1, lt + 1):
        if S[i - 1] == T[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
i = ls
j = lt
ans = ""

while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans = S[i - 1] + ans
        i -= 1
        j -= 1

print(ans)


