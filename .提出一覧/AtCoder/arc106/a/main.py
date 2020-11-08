#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())

A = 1
while 3 ** A < N:
    B = 0
    n = N - 3 ** A
    while n % 5 == 0:
        n //= 5
        B += 1
    if n == 1 and B > 0:
        print(A, B)
        exit()

    A += 1

print(-1)