#!/usr/bin/env python3

import heapq
N, M = map(int, input().split())
ab, ac, bc = map(int, input().split())
S = list(input())
ABC = [list(map(int, input().split())) for _ in range(M)]

G = {i: [] for i in range(N)}

for abc in ABC:
    a = abc[0]
    b = abc[1]
    c = abc[2]
    a -= 1; b -= 1
    G[a].append([b, c])
    G[b].append([a, c])

A = -1; B = -1; C = -1

if S[0] == "A":
    A = 0
elif S[0] == "B":
    B = 0
else:
    C = 0

dist = [10 ** 15] * N
dist[0] = 0
seen = [False] * N

hq = [(0, 0)]

for i in range(1, N):
    if S[0] == S[i]:
        continue

    t = 0

    if S[0] == "A":
        if S[i] == "B":
            t = ab
        else:
            t = ac
    elif S[0] == "B":
        if S[i] == "A":
            t = ab
        else:
            t = bc
    else:
        if S[i] == "A":
            t = ac
        else:
            t = bc

    dist[i] = t
    heapq.heappush(hq, (t, i))

# print(dist)
while hq:
    # print(hq)
    v = heapq.heappop(hq)[1]

    if seen[v]:
        continue

    # print(v)
    seen[v] = True

    if S[v] == "A":
        if B != -1:
            dist[v] = min(dist[v], dist[B] + ab)
        if C != -1:
            dist[v] = min(dist[v], dist[C] + ac)

        if A == -1 or dist[v] < dist[A]:
            A = v
            seen = [False] * N

            heapq.heappush(hq, (0, 0))

    elif S[v] == "B":
        if A != -1:
            dist[v] = min(dist[v], dist[A] + ab)
        if C != -1:
            dist[v] = min(dist[v], dist[C] + bc)

        if B == -1 or dist[v] < dist[B]:
            B = v
            seen = [False] * N

            heapq.heappush(hq, (0, 0))

    else:
        if A != -1:
            dist[v] = min(dist[v], dist[A] + ac)
        if B != -1:
            dist[v] = min(dist[v], dist[B] + bc)

        if C == -1 or dist[v] < dist[C]:
            C = v
            seen = [False] * N

            heapq.heappush(hq, (0, 0))

    for g in G[v]:
        if seen[g[0]] == False:
            dist[g[0]] = min(dist[g[0]], dist[v] + g[1])
            heapq.heappush(hq, (dist[g[0]], g[0]))

# print(dist)
print(dist[-1])
