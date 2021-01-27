#!/usr/bin/env python3

#import
import math
#import numpy as np
N = int(input())

t = 1

for i in range(2, N + 1):
    t = (t * i) // math.gcd(t, i)

ans = t

while ans < N:
    ans += t

print(ans + 1)