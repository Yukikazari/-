#!/usr/bin/env python3

import copy
#import math
#import numpy as np
N = int(input())
S = input()

cnt = 0
fox = 0

li = [[0] * 2 for _ in range(N + 1)]

for i in range(N):
    if S[i] == "f":
        cnt += 1
        li[cnt][0] = 1
        li[cnt][1] = 0

    elif S[i] == "o":
        if li[cnt][0] and not li[cnt][1]:
            li[cnt][1] = 1
        else:
            cnt = 0
    elif S[i] == "x":
        if li[cnt][0] and li[cnt][1]:
            fox += 1
            cnt -= 1
        else:
            cnt = 0
    else:
        cnt = 0

print(N - fox * 3)