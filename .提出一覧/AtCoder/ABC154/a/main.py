#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()

if S == U:
    print(A - 1, B)
else:
    print(A, B - 1)
