#!/usr/bin/env python3

import copy
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if S[i][j] == ".":
            continue

        S2 = copy.deepcopy(S)
        S2[i][j] = "."

        vil = [[False] * M for _ in range(N)]

        que = [i * M + j]
        while len(que) > 0:
            a = que[0] // M
            b = que[0] % M
            que.pop(0)

            vil[a][b] = True
            if a > 0 and S2[a - 1][b] == "." and not vil[a - 1][b]:
                que.append((a - 1) * M + b)
                vil[a - 1][b] = True
            if a < N - 1 and S2[a + 1][b] == "." and not vil[a + 1][b]:
                que.append((a + 1) * M + b)
                vil[a + 1][b] = True
            if b > 0 and S2[a][b - 1] == "." and not vil[a][b - 1]:
                que.append((a) * M + b - 1)
                vil[a][b - 1] = True
            if b < M - 1 and S2[a][b + 1] == "." and not vil[a][b + 1]:
                que.append((a) * M + b + 1)
                vil[a][b + 1] = True

        isok = True

        for k in range(N):
            for l in range(M):
                if S2[k][l] == "." and not vil[k][l]:
                    isok = False

        if isok:
            ans += 1

print(ans)