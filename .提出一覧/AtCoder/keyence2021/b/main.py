#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = {i:0 for i in range(300005)}

for a in A:
    dic[a] += 1

ans = 0
box = K

for i in range(300005):
    if dic[i] == 0:
        ans += box * i
        break

    elif dic[i] >= box:
        continue

    else:
        ans += (box - dic[i]) * i
        box = dic[i]

    if box <= 0:
        break

print(ans)