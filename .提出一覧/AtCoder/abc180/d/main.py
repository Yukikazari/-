#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
X, Y, A, B = map(int, input().split())

ans = 0

while X < Y and X * A < X + B:
    ans += 1
    X *= A

ans += (Y - X - 1) // B

print(ans)
