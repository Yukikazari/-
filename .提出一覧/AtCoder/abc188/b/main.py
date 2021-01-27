#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))
B  = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans += A[i] * B[i]

print("Yes" if ans == 0 else "No")