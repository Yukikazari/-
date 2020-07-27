N = int(input())

A = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1000

for i in range(1, N):
    dp[i] = dp[i - 1]
    t = dp[i - 1] + (A[i] - A[i - 1]) * (dp[i - 1] // A[i - 1])
    dp[i] = max(dp[i], t)

print(dp[-1])
