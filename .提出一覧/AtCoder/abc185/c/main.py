#!/usr/bin/env python3

#import
#import math
#import numpy as np
L = int(input())

if L == 12:
    print(1)
    exit()

ans = 1

for i in range(1, 12):
    ans *= L - i

for i in range(2, 12):
    ans //= i

print(ans)