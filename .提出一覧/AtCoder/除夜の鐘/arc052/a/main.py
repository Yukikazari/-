#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = list(input())

ans = ""
for s in S:
    if s.isdecimal():
        ans += s
    elif ans != "":
        break

print(ans)
