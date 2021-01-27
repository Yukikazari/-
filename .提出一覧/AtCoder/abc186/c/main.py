#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())

ans = 0

def ten(num):
    isok = True
    while num > 0:
        if num % 10 == 7:
            isok = False
            break
        num //= 10

    return isok

def eight(num):
    isok = True
    while num > 0:
        if num % 8 == 7:
            isok = False
            break
        num //= 8

    return isok

for i in range(1, N + 1):
    if ten(i) and eight(i):
        ans += 1

print(ans)