#!/usr/bin/env python3

#import
#import math
#import numpy as np
X = int(input())

m = 100
ans = 0
while m < X:
    m = m * 101 // 100
    ans += 1

print(ans)