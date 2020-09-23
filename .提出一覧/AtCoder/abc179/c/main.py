#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())

nn = N - 1

ans = 0

for i in range(1, N):
    ans += nn // i

print(ans)
