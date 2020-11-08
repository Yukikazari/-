#!/usr/bin/env python3

#import
#import math
#import numpy as np
T = int(input())
#= input()
#= map(int, input().split())
#= list(map(int, input().split()))
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    ans = False
    
    if N % 2 == 0:
        t = 0
        for a in A:
            t = t ^ a

        if t != 1:
            ans = True

    if ans:
        print("First")
    else:
        print("Second")
