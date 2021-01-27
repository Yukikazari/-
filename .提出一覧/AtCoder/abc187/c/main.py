#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())

one = []
zero = []

for _ in range(N):
    S = input()

    if S[0] == "!":
        one.append(S[1:])
    else:
        zero.append(S)

one.sort()
zero.sort()

i = 0; j = 0

while i < len(one) and j < len(zero):
    if one[i] == zero[j]:
        print(one[i])
        exit()

    if one[i] < zero[j]:
        i += 1
    else:
        j += 1

print("satisfiable")



