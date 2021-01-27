#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
D = list(map(int, input().split()))

ans = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        ans += D[i] * D[j]

print(ans)