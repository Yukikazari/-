#!/usr/bin/env python3

import itertools
#import math
#import numpy as np
N = int(input())
S = input()

li = itertools.permutations(S)

for l in li:
    s = "".join(l)
    if s != S and s[::-1] != S:
        print(s)
        exit()

print("None")