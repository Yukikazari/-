#!/usr/bin/env python3

#import
import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

if M == 0:
    print(1)
    exit()

if N == M:
    print(0)
    exit()

r = A[0] - 1 if A[0] != 1 else 10 ** 9

for i in range(M - 1):
    if A[i + 1] - A[i] == 1:
        continue

    r = min(r, A[i + 1] - A[i] - 1)

if A[-1] != N:
    r = min(r, N - A[-1])

ans = 0

ans += math.ceil((A[0] - 1) / r)

for i in range(M - 1):
    ans += math.ceil((A[i + 1] - A[i] - 1) / r)

ans += math.ceil((N - A[-1]) / r)

print(ans)