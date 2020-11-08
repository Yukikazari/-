#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())
S = [input() for _ in range(N)]
K -= 1
dic = {}

for s in S:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

dic2 = sorted(dic.items(), key=lambda x: x[1], reverse = True)

isok = True

if K > 0 and dic2[K][1] == dic2[K - 1][1]:
    isok = False
if K < len(dic2) - 1 and dic2[K][1] == dic2[K + 1][1]:
    isok = False

if isok:
    print(dic2[K][0])
else:
    print("AMBIGUOUS")
