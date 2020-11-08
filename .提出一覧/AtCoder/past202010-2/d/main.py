#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
S = input()

xy = 0
tmp = 0
for s in S:
    if s == ".":
        tmp += 1
    else:
        xy = max(xy, tmp)
        tmp = 0
xy = max(xy, tmp)

st = 0; en = 0
for i in range(N):
    if S[i] == ".":
        st += 1
    else:
        break
for i in range(N - 1, -1, -1):
    if S[i] == ".":
        en += 1
    else:
        break

if st + en < xy:
    st += xy - (st + en)

print(st, en)