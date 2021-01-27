#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, C = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]

dic = {}

for abc in ABC:
    a, b, c = abc

    if a in dic:
        dic[a] += c
    else:
        dic[a] = c
    
    if b + 1 in dic:
        dic[b + 1] -= c
    else:
        dic[b + 1] = -c

keys = list(dic.keys())
keys.sort()

ans = 0
cnt = 0

for i in range(len(keys) - 1):
    a = keys[i]
    b = keys[i + 1]
    cnt += dic[keys[i]]

    ans += min(cnt, C) * (b - a)
    # print(ans, a, b)

print(ans)
# print(dic)