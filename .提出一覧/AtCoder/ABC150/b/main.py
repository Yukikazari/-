#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
S = input()

ans = 0

for i in range(3, N + 1):
    if S[i - 3 :i] == "ABC":
        ans += 1

print(ans)