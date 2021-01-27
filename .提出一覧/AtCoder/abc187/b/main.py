#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
xy= [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        xi = xy[i][0]; yi = xy[i][1]
        xj = xy[j][0]; yj = xy[j][1]

        if abs((yj - yi) / (xj - xi)) <= 1:
            ans += 1

print(ans)
