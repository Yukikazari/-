N = int(input())

G = [list() for i in range(N)]
edge = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
    edge.append([a, b])

depth = [-1] * N
depth[0] = 0
que = [0]
while que:
    q = que.pop()
    for a in G[q]:
        if depth[a] == -1:
            depth[a] = depth[q] + 1
            que.append(a)

Q = int(input())

li = [0] * N

for _ in range(Q):
    t, e, x = map(int, input().split())
    e -= 1
    ae, be = edge[e]

    if t == 2:
        ae, be = be, ae

    if depth[ae] > depth[be]:
        li[ae] += x
    else:
        li[0] += x
        li[be] -= x

# print(li)

que = [0]

while que:
    q = que.pop()

    for a in G[q]:
        if depth[a] > depth[q]:
            li[a] += li[q]
            que.append(a)

for i in li:
    print(i)