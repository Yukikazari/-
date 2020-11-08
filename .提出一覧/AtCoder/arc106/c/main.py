#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
if M == 0:
    for i in range(1, N + 1):
        print(i * 2, i * 2 + 1)

elif M > 0 and N - abs(M) > 1:
    m = abs(M)
    print(1, m * 2 + 5)
    for i in range(m + 1):
        print(i * 2 + 2, i * 2 + 3)
        
    for i in range(N - m - 2):
        print(i * 2 + m * 2 + 10, i * 2 + m * 2 + 11)

else:
    print(-1)