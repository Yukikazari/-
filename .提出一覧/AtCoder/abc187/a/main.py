#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
A, B = map(str, input().split())

a = 0; b = 0

for aa in A:
    a += int(aa)
for bb in B:
    b += int(bb)

print(max(a, b))