N, M = map(int, input().split())

G = {i: [] for i in range(1, N + 1)}

for i in range(M):
    a, b = map(int, input().split())
    if a == 1 or a == N or b == 1 or b == N:
        G[a].append(b)
        G[b].append(a)

res = False

for i in range(2, N):
    if 1 in G[i] and N in G[i]:
        res = True
        break


if res:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")