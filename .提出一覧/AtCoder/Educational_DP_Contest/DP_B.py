# Python:TLE PyPy:AC

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())
h = list(map(int, input().split()))
#= [input(), input()]

dp = [0] * N

dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    t = dp[i - 1] + abs(h[i] - h[i - 1])
    for j in range(2, min(K + 1, i + 1)):
        tt = dp[i - j] + abs(h[i] - h[i - j])
        t = min(t, tt)

    dp[i] = t

print(dp[-1])