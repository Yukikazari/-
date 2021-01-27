#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
A = list(map(int, input().split()))

ans = True

for a in A:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            ans = False

if ans:
    print("APPROVED")

else:
    print("DENIED")

