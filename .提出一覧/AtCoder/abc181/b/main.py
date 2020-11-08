#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for ab in AB:
    a = ab[0]
    b = ab[1]

    ans += (a + b) * (b - a + 1) // 2

print(ans)

