#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
n, k = map(int, input().split())
s = input()

rps = s

for _ in range(k):
    tmp = ""
    for i in range(n):
        t1 = rps[(i * 2) % n]; t2 = rps[(i * 2 + 1) % n]

        if (t1 == "R" and t2 == "P") or (t1 == "P" and t2 == "R") or (t1 == t2 == "P"):
            tmp += "P"
        elif (t1 == "S" and t2 == "P") or (t1 == "P" and t2 == "S") or (t1 == t2 == "S"):
            tmp += "S"
        else:
            tmp += "R"

    rps = tmp

print(rps[0])