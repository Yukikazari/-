#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = input()

a = ["U", "D"]

for i in range(len(S)):
    s = S[i]

    if s not in a:
        if i % 2 == 0 and s != "R":
            print("No")
            exit()

        elif i % 2 == 1 and s != "L":
            print("No")
            exit()
print("Yes")