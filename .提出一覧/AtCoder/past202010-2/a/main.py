#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
a, b, c = map(int, input().split())

if a < b < c or c < b < a:
    print("B")
elif b < a < c or c < a < b:
    print("A")
else:
    print("C")

