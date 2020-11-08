#!/usr/bin/env python3

#import
import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
A = list(map(int, input().split()))

asum = sum(A)
ok = math.ceil(asum / (4 * M))

ans = 0
for a in A:
    if a >= ok:
        ans += 1

if ans >= M:
    print("Yes")
else:
    print("No")
