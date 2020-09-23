#import
import math
#import numpy as np
modnum = 10 ** 9 + 7
S = int(input())

def mod(num):
    return num % modnum

dp = [0] * (S + 20)
dp[0] = 1

for i in range(S + 10):
    for j in range(3, 10):
        dp[i + j] = mod(dp[i + j] + dp[i])


print(dp[S])


