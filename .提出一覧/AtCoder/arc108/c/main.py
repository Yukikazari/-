#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
UVC = [list(map(int, input().split())) for _ in range(M)]

G = {i: [] for i in range(N)}

que = []
for uvc in UVC:
    u = uvc[0] - 1
    v = uvc[1] - 1
    c = uvc[2]

    G[u].append([v, c])
    G[v].append([u, c])

ans = [0] * N
seen = [False] * N
ng = [0] * N

que.append(0)

while len(que):
    q = que.pop(0)
    if seen[q]:
        continue

    for g in G[q]:
        c = g[1]
        if c in ng[q]:
            continue
        ans[q] = c
        break

    if ans[q]:
        for g in G[q]:
            u = g[0]
            ng[u].append(ans[q])





