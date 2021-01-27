#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
S = [list(input()) for _ in range(N)]

R = 0; B = 0

for s in S:
    R += s.count("R")
    B += s.count("B")

if R > B:
    print("TAKAHASHI")
elif R < B:
    print("AOKI")
else:
    print("DRAW")