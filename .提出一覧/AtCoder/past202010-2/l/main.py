#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, Q = map(int, input().split())
H = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]

dic = {}

for i in range(N - 1):
    t = H[i + 1] - H[i]
    if i % 2 == 1:
        t *= -1
    if t in dic:
        dic[t] += 1
    else:
        dic[t] = 1
# print(dic)
# exit()
cnt = 0

for q in Query:
    if q[0] == 1:
        cnt += q[1]
    elif q[0] == 2:
        cnt -= q[1]
    else:
        u = q[1]; v = q[2]
        u -= 1

        if u > 0:
            t = H[u] - H[u - 1]
            if u % 2 == 0:
                t *= - 1
            dic[t] -= 1
        if u < N - 1:
            t = H[u + 1] - H[u]
            if u % 2 == 1:
                t *= - 1
            dic[t] -= 1

        H[u] += v

        if u > 0:
            t = H[u] - H[u - 1]
            if u % 2 == 0:
                t *= - 1
            if t in dic:
                dic[t] += 1
            else:
                dic[t] = 1
        if u < N - 1:
            t = H[u + 1] - H[u]
            if u % 2 == 1:
                t *= - 1
            if t in dic:
                dic[t] += 1
            else:
                dic[t] = 1

    if cnt in dic:
        print(max(dic[cnt], 0))
    else:
        print(0)