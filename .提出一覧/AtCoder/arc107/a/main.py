#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
a, b, c= map(int, input().split())

aa = a * (a + 1) // 2 % 998244353
bb = b * (b + 1) // 2 % 998244353
cc = c * (c + 1) // 2 % 998244353

print((aa * bb * cc) % 998244353)
