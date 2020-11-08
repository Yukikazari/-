#!/usr/bin/env python3

#import
import math
#import numpy as np
#= int(input())
#= input()
x, y = map(int, input().split())

if y == 0:
    print("ERROR")
    exit()

ans = 100 * x // y
ans /= 100

print("{:.2f}".format(ans))
