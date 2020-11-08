#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
S = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        ans = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                if not 0 <= i + k < N or not 0 <= j + l < M:
                    continue
                
                if S[i + k][j + l] == "#":
                    ans += 1

        print(ans, end="")
    print()
