N, M = map(int, input().split())

res = [0] * (M + 1)

for _ in range(N):
    A = list(map(int, input().split()))
    K = A.pop(0)
    for a in A:
        res[a] += 1

ans = 0

for r in res:
    if r == N:
        ans += 1

print(ans)