#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

Amin = 10 ** 9
Asum = 0
for a in A:
    Amin = min(Amin, min(a))
    Asum += sum(a)

print(Asum - h * w * Amin)