#!/usr/bin/env python3

import itertools
#import math
#import numpy as np
#= int(input())
S = list(input())

dic = {i:0 for i in range(10)}

for s in S:
    dic[int(s)] += 1

ans = False

if len(S) < 3:
    t = list(itertools.permutations(S))

    for tt in t:
        n = int("".join(tt))
        if n % 8 == 0:
            ans = True
            break

else:
    for i in range(125):
        j = i * 8
        t = list(str(j).zfill(3))
        isok = True
        for k in range(10):
            if t.count(str(k)) > dic[k]:
                isok = False
        if isok:
            ans = True
            break
        

if ans:
    print("Yes")
else:
    print("No")