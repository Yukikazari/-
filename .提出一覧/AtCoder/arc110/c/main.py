#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
P = list(map(int, input().split()))

dic = {i: 0 for i in range(1, N + 1)}
small = 1; large = N

for i in range(N):
    dic[P[i]] = i + 1

ans = True
al = list()
ad = {i:False for i in range(1, N)}

# print(dic)

while small != large:
    # dic[hoge] : 1-indexed
    # P[di - 1] : small
    di = dic[small]
    if small != di:
        P[di - 1], P[di - 2] = P[di - 2], P[di - 1]
        # print(P)
        dic[P[di - 1]] = di
        dic[P[di - 2]] = di - 1
        if ad[di - 1]:
            ans = False
            break
        al.append(di - 1)
        ad[di - 1] = True

    if small == dic[small]:
        small += 1
        ns = False

    # print(al)
    # print(dic)

for i in range(1, N):
    ans = ans and ad[i]


if ans:
    for a in al:
        print(a)

else:
    print(-1)