#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, X = map(int, input().split())
S = input()

ans = X

for i in range(N):
    if S[i] == "o":
        ans += 1
    else:
        ans = max(ans - 1, 0)

print(ans)