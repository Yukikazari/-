#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = input()
ans = 0

for i in range(len(S)):
    if S[i] != S[-(i + 1)]:
        ans += 1

print(ans // 2)