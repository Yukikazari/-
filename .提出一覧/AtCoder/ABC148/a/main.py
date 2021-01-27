#!/usr/bin/env python3

#import
#import math
#import numpy as np
A = [int(input()) for _ in range(2)]

for i in range(1, 4):
    if i not in A:
        print(i)
        exit()
