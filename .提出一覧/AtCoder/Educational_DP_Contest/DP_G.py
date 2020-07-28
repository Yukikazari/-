import sys
sys.setrecursionlimit(10**7)

def dfs(num):
    if dp[num] != -1:
        return dp[num]

    res = 0
    for obj in G[num]:
        res = max(res, dfs(obj) + 1)

    dp[num] = res
    return res


N, M = map(int, input().split())

dp = [-1] * N
G = {i:[] for i in range(N)}

for _ in range(M):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)

res = 0
for i in range(N):
    res = max(res, dfs(i))

print(res)