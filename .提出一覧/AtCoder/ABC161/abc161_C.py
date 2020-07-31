N, K = map(int, input().split())

t = N % K

res = min(t, K - t)

print(res)