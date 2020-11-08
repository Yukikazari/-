#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
P = list(map(int, input().split()))

dic = {i:False for i in range(200001)}
now = 0

for p in P:
    dic[p] = True
    for i in range(now, 10 ** 9):
        if not dic[i]:
            now = i
            print(i)
            break