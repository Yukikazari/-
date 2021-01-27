#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

t = 2 ** N

t1 = 0; t2 = t // 2

for i in range(t):
    if i < t // 2:
        if A[t1] < A[i]:
            t1 = i
    else:
        if A[t2] < A[i]:
            t2 = i

print(t1 + 1 if A[t1] < A[t2] else t2 + 1)