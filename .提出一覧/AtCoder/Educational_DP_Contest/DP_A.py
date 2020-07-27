#import math
#import numpy as np

N =int(input())
#=input()
#=map(int, input().split())
h =list(map(int, input().split()))
#=[input(), input()]

dp = [0] * N
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    t1 = dp[i - 1] + abs(h[i] - h[i - 1])
    t2 = dp[i - 2] + abs(h[i] - h[i - 2])
    dp[i] = min(t1, t2)

print(dp[-1])