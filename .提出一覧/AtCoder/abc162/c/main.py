#!/usr/bin/env python3

#import
import math
#import numpy as np
K = int(input())

ans = 0

for i in range(1, K + 1):
    for j in range(1, K + 1):
        t = math.gcd(i, j)
        for k in range(1, K + 1):
            ans += math.gcd(t, k)

print(ans)