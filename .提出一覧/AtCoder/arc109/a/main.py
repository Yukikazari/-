#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
a, b, x, y = map(int, input().split())

if a == b:
    print(x)

elif a > b:
    t = a - b - 1
    print(x + min(t * y, t * 2 * x))

else:
    t = b - a
    print(x + min(t * y, t * 2 * x))