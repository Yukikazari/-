#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())

for i in range(1, 10 ** 6):
    if K ** i > N:
        print(i)
        exit()

