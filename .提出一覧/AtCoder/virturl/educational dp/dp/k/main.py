#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (K + 1)

for i in range(K + 1):
    for a in A:
        if i >= a:
            dp[i] = not dp[i - a] or dp[i]

if dp[K]:
    print("First")
else:
    print("Second")
