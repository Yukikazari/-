#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
last = -2

for i in range(N):
    a = A[i] - 1
    ans += B[a]
    if a - last == 1:
        ans += C[last]

    last = a
    # print(ans)

print(ans)

