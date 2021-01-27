#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

A.sort()
Asum = [0] * N
Asum[0] = A[0]
for i in range(1, N):
    Asum[i] = Asum[i - 1] + A[i]

ans = 0

for i in range(N - 1, 0, -1):
    ans += A[i] * (i) - Asum[i - 1]

print(ans)