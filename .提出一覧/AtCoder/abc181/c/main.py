#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XY.sort()

for i in range(N - 2):
    xi = XY[i][0]
    yi = XY[i][1]
    for j in range(i + 1, N - 1):
        xj = XY[j][0]
        yj = XY[j][1]
        for k in range(j + 1, N):
            xk = XY[k][0]
            yk = XY[k][1]

            if (xk - xi) * (yj - yi) == (xj - xi) * (yk - yi):
                print("Yes")
                exit()

print("No")
