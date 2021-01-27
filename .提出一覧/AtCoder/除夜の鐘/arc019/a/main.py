#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = list(input())

dic = {"O": 0, "D": 0, "I": 1, "Z": 2, "S": 5, "B": 8}

for i in range(len(S)):
    if S[i] in dic:
        S[i] = str(dic[S[i]])

print("".join(S))