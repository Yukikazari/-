#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, W = map(int, input().split())
STP = [list(map(int, input().split())) for _ in range(N)]

water = [0] * (10 ** 6)

for stp in STP:
    s = stp[0]; t = stp[1]; p = stp[2]

    water[s] += p
    water[t] -= p
# print(water[:20])
ans = water[0] <= W

for i in range(1, 10 ** 6):
    water[i] += water[i - 1]

    if water[i] > W:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")

# print(water[:20])