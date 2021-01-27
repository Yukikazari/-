#!/usr/bin/env python3

import itertools
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

li = [i for i in range(1, N)]

per = list(itertools.permutations(li))

ans = 0

for p in per:
    t = T[0][p[0]] + T[p[-1]][0]
    for i in range(N - 2):
        # print(p[i - 1], p[i])
        t += T[p[i]][p[i + 1]]

    if t == K:
        ans += 1

print(ans)

