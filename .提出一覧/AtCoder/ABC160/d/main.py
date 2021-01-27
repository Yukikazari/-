#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, X, Y = map(int, input().split())
X -= 1; Y -= 1

dic = {i:0 for i in range(N + 1)}

for i in range(N - 1):
    for j in range(i + 1, N):
        t = min(abs(j - i), abs(X - i) + abs(Y - j) + 1, abs(Y - i) + abs(X - j) + 1)
        # print(i, j, t)
        
        dic[t] += 1

for i in range(1, N):
    print(dic[i])

