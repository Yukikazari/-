#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

now = N

time = 0

for ab in AB:
    a = ab[0]
    b = ab[1]

    now -= a - time

    if now <= 0:
        print("No")
        exit()

    now = min(now + (b - a), N)
    time = b
now -= T - b

print("Yes" if now > 0 else "No")