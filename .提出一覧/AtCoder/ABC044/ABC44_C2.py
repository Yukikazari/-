import numpy as np

n, a = map(int, input().split())
x = list(map(int, input().split()))
MAX = 50 * n

# dp = [[0]*(MAX+1) for _ in range(n+1)]
dp = np.zeros((n + 1, MAX + 1), np.int64)
dp[0][0] = 1

for e in x:
    dp[1:, e:] += dp[:-1, :-e]
    print(dp[1:, e:])

cnt = np.arange(1, n + 1)
sm = cnt * a
ans = dp[cnt, sm].sum()

print(ans)
