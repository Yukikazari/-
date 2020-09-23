#import
#import math
#import numpy as np
N = int(input())
XY= [list(map(int, input().split())) for _ in range(N)]

pmaxint = -10**10
pminint = 10**10
mmaxint = -10**10
mminint = 10**10

for x, y in XY:
    t1 = x + y
    t2 = x - y
    if t1 > pmaxint:
        pmaxint = t1
    if t1 < pminint:
        pminint = t1
    
    if t2 > mmaxint:
        mmaxint = t2
    if t2 < mminint:
        mminint = t2

print(max(abs(pmaxint - pminint), abs(mmaxint - mminint)))