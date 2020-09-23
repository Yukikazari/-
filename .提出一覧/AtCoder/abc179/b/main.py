#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
D = [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

zoro = 0

for d1, d2 in D:
    if d1 == d2:
        zoro += 1
    else:
        zoro = 0

    if zoro == 3:
        print("Yes")
        exit()

print("No")