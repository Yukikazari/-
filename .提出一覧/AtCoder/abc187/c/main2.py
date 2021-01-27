#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())

a = set()
b = set()

for _ in range(N):
    S = input()

    if S[0] == "!":
        a.add(S[1:])
    else:
        b.add(S)

for obj in a:
    if obj in b:
        print(obj)
        exit()

print("satisfiable")
