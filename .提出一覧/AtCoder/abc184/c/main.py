#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r = abs(r2 - r1)
c = abs(c2 - c1)

if r == c:
    if r == 0:
        print(0)
    else:
        print(1)

elif abs(r - c) <= 3:
    if (r + c) <= 3:
        print(1)
    else:
        print(2)

else:
    if abs(r - c) % 2 == 0:
        print(2)
    else:
        print(3)

