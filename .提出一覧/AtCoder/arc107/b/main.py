#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())

ans = 0
K = abs(K)
for i in range(2, N * 2 + 1):
    if i - K < 2:
        continue

    t1 = min(i - 1, 2 * N - i + 1)
    t2 = min((i - K) - 1, 2 * N - (i - K) + 1)
    

    ans += t1 * t2

print(ans)
