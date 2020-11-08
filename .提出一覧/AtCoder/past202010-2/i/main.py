#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

Asum = sum(A)
A.extend(A)

st = 0; en = 0
x = 0

ans = Asum

while st <= N:
    if 2 * x < Asum:
        x += A[en]
        en += 1        
    else:
        x -= A[st]
        st += 1

    y = Asum - x

    ans = min(ans, abs(y - x))

print(ans)
