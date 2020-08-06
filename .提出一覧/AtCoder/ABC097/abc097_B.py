import math

X = int(input())

dp = [[0] * 100 for _ in range(X + 1)]

maxint = 1

for i in range(2, int(math.sqrt(X)) + 1):
    dp[i][1] = i
    for j in range(2, 100):
        dp[i][j] = dp[i][j - 1] * i
        if dp[i][j] > X:
            maxint = max(maxint, dp[i][j - 1])
            break
            

print(maxint)