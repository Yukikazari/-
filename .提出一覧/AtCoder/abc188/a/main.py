#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
#= map(int, input().split())
X = list(map(int, input().split()))
X.sort()

if X[1] - X[0] < 3:
    print("Yes")
else:
    print("No")
