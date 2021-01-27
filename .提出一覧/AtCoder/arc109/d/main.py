#!/usr/bin/env python3

#import
#import math
#import numpy as np
T = int(input())
#= input()
#= map(int, input().split())

for _ in range(T):
    ax, ay, bx, by, cx, cy = map(int, input().split())

    x = min(ax, bx, cx)
    y = min(ay, by, cy)

    xy = [[ax, ay], [bx, by], [cx, cy]]

    ans = 0
    ans += abs(abs(x) - abs(y)) * 2

    if x == 0 and y == 0:
        if [x + 1, y + 1] in xy:
            ans = 1
    else:
        if x >= 0 and y >= 0:
            t = min(abs(x), abs(y))
            if t > 0:
                ans += 1 + t * 2


        elif x >= 0 and y < 0:
            if not [x, y] in xy or not [x, y + 1] in xy:
                ans += 1
        elif x < 0 and y >= 0:
            if not [x + 1, y] in xy or not [x + 1, y + 1] in xy:
                ans += 1
        else:
            if not [x, y + 1] in xy or not [x + 1, y + 1] in xy:
                ans += 1

    print(ans)