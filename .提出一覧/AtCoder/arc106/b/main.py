#!/usr/bin/env python3

from atcoder.dsu import DSU
#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = [list(map(int, input().split())) for _ in range(M)]

cnt = [0] * N
for i in range(N):
    cnt[i] = B[i] - A[i]

uf = DSU(N)

for cd in CD:
    c = cd[0]
    d = cd[1]
 
    uf.merge(c - 1, d - 1)
    
al = uf.groups()

ans = True
for li in al:
    t = 0
    for d in li:
        t += cnt[d]

    if t != 0:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")