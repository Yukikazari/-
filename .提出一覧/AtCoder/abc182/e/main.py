#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
H, W, N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

lh = {i:[] for i in range(H)}
lw = {i:[] for i in range(W)}
bh = {i:[] for i in range(H)}
bw = {i:[] for i in range(W)}

for ab in AB:
    a = ab[0] - 1
    b = ab[1] - 1
    lh[a].append(b)
    lw[b].append(a)

for cd in CD:
    c = cd[0] - 1
    d = cd[1] - 1
    bh[c].append(d)
    bw[d].append(c)

floor = [[0] * W for _ in range(H)]

for i in range(H):
    ll = len(lh[i])
    bl = len(bh[i])
    tmp = [0] * W

    if ll > 0 and bl == 0:
        for j in range(W):
            floor[i][j] = 1
    elif ll == 0:
        continue
    else:
        for l in lh[i]:
            tmp[l] = 1
        for b in bh[i]:
            tmp[b] = -1

        for j in range(1, W):
            if tmp[j] == 0 and tmp[j - 1] == 1:
                tmp[j] = 1
        for j in range(W - 2, -1, -1):
            if tmp[j] == 0 and tmp[j + 1] == 1:
                tmp[j] = 1

        for j in range(W):
            floor[i][j] = max(floor[i][j], tmp[j])

    # print(i, tmp)

# print()

for j in range(W):
    ll = len(lw[j])
    bl = len(bw[j])
    tmp = [0] * H

    if ll > 0 and bl == 0:
        for i in range(H):
            floor[i][j] = 1
    elif ll == 0:
        continue
    else:
        for l in lw[j]:
            tmp[l] = 1
        for b in bw[j]:
            tmp[b] = -1

        for i in range(1, H):
            if tmp[i] == 0 and tmp[i - 1] == 1:
                tmp[i] = 1
        for i in range(H - 2, -1, -1):
            if tmp[i] == 0 and tmp[i + 1] == 1:
                tmp[i] = 1

        for i in range(H):
            floor[i][j] = max(floor[i][j], tmp[i])

ans = 0
for i in range(H):
    ans += floor[i].count(1)

print(ans)

