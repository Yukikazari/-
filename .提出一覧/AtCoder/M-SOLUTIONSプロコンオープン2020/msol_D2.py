N = int(input())

A = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1000

for i in range(1, N):
    dp[i] = dp[i - 1]
    for j in range(i):
        kabu = dp[j] // A[j]
        money = dp[j] + (A[i] - A[j]) * kabu
        dp[i] = max(dp[i], money)

print(dp[-1])