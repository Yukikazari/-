#import
#import math
#import numpy as np
#= int(input())
#= input()
#= map(int, input().split())
#= [input(), input()]

s = input()
t = input()

sl = len(s)
tl = len(t)

dp = [[0] * (tl + 1) for _ in range(sl + 1)]

for i in range(1, sl + 1):
    for j in range(1, tl + 1):
        if s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])

res = ""
i = sl
j = tl  
while i > 0 and j > 0:
    if dp[i - 1][j] == dp[i][j]:
        i -= 1

    elif dp[i][j - 1] == dp[i][j]:
        j -= 1

    else:
        res = s[i - 1] + res
        i -= 1
        j -= 1

print(res)