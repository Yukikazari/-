#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

dic = {}

for a in A:
    if a in dic:
        print("NO")
        exit()

    dic[a] = True

print("YES")

