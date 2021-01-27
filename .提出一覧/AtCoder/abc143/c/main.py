#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
S = list(input())

ans = 0

for i in range(1, N):
    if S[i - 1] != S[i]:
        ans += 1

print(ans + 1)