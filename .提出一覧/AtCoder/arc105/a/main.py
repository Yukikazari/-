#!/usr/bin/env python3

#import
#import math
#import numpy as np
A = list(map(int, input().split()))
a = sum(A)

for i in range(2 ** 4):
    t = []
    for j in range(4):
        if (i >> j) & 1:
            t.append(j)
    cnt = 0
    for tt in t:
        cnt += A[tt]

    if cnt * 2 == a:
        print("Yes")
        exit()

print("No")
