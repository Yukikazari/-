#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
S = list(input())

for s in S:
    print(chr(ord("A") + (ord(s) + N - ord("A")) % 26), end="")
print()