#!/usr/bin/env python3

#import
import math
#import numpy as np
#= int(input())
#= input()
a, b, c, d = map(int, input().split())

print("Yes" if math.ceil(a / d) >= math.ceil(c / b) else "No")
