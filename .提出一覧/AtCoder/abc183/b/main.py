#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
sx, sy, gx, gy= map(int, input().split())

gy *= - 1

a = (gy - sy) / (gx - sx) * -1

print(sx + sy / a)