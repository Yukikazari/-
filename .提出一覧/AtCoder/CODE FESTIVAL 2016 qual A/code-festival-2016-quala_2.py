N = int(input())
A = list(map(int, input().split()))

G = {i:[] for i in range(1, N + 1)}

res = 0

for i, a in enumerate(A, 1):
    if i in G[a]:
        res += 1

    G[a].append(i)
    G[i].append(a)

print(res)
