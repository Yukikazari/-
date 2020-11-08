#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
XYZ = [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

cost = [[10 ** 9] * N for _ in range(N)]
for i in range(N):
    xi = XYZ[i][0]
    yi = XYZ[i][1]
    zi = XYZ[i][2]
    for j in range(N):
        if i == j:
            continue

        xj = XYZ[j][0]
        yj = XYZ[j][1]
        zj = XYZ[j][2]

        cost[i][j] = abs(xj - xi) + abs(yj - yi) + max(0, zj - zi)


