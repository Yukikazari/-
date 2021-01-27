#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [0] * N
b = [0] * N

a[0] = A[0]
b[0] = B[0]
for i in range(1, N):
    a[i] = max(a[i - 1], A[i])
    b[i] = max(b[i - 1], B[i])

ans = a[0] * b[0]

for i in range(N):
    ans = max(ans, a[i] * B[i])
    print(ans)