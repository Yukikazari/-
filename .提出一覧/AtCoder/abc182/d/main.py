#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

B = [0] * (N + 1)
for i in range(N):
    B[i + 1] = B[i] + A[i]

C = [0] * (N + 1)

for i in range(1, N + 1):
    C[i] = C[i - 1] + B[i]

ans = N - 1
cnt = 0

for i in range(N - 1, -1, -1):
    if C[i] > C[ans]:
        ans = i

print(max(C[ans] + max(B[:ans + 1]), C[N]))
