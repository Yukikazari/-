#!/usr/bin/env python3

#import
#import math
#import numpy as np
X = int(input())

d, r = divmod(X, 500)

print(d * 1000 + r // 5 * 5)
