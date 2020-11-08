#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

dic = {i: 0 for i in range(1, N + 1)}

for a in A:
    dic[a] += 1

for k in dic:
    print(dic[k])
