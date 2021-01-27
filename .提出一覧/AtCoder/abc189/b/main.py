#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]

alc = 0
X *= 100

for i in range(N):
    v, p = VP[i]
    alc += v * p

    if alc > X:
        print(i + 1)
        exit()

print(-1)


