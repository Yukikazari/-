#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

li = []
aoki = 0

for ab in AB:
    a = ab[0]; b = ab[1]
    li.append(a * 2 + b)
    aoki += a

li.sort()

chokudai = 0

for i in range(1, len(li) + 1):
    chokudai += li[-i]

    if chokudai > aoki:
        print(i)
        exit()