N = int(input())
P = list(map(int, input().split()))

dp = [0] * N

dp[0] = P[0]

for i in range(1, N):
    dp[i] = min(dp[i - 1], P[i])

res = 0
for i in range(N):
    if dp[i] >= P[i]:
        res += 1

print(res)