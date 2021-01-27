#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

dic = {i: 0 for i in range(1, 1001)}

for a in A:
    for i in range(2, a + 1):
        if a % i == 0:
            dic[i] += 1

ans = 1

for i in range(2, 1001):
    if dic[ans] <= dic[i]:
        ans = i

print(ans)