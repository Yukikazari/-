#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0

AB.reverse()

for a, b in AB:
    if (a + ans) % b != 0:
        ans += b - (a + ans) % b

print(ans)