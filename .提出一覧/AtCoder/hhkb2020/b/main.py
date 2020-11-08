#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0

for i in range(H):
    for j in range(W):
        if i < H - 1 and S[i][j] == S[i + 1][j] == ".":
            ans += 1
        if j < W - 1 and S[i][j] == S[i][j + 1] == ".":
            ans += 1

print(ans)