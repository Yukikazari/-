#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
H = list(map(int, input().split()))
#= [input(), input()]
AB= [list(map(int, input().split())) for _ in range(M)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

G = {i: set() for i in range(N)}

mx = [0] * N

for a, b in AB:
    mx[a - 1] = max(mx[a - 1], H[b - 1])
    mx[b - 1] = max(mx[b - 1], H[a - 1])

ans = 0

for i in range(N):
    if H[i] > mx[i]:
        ans += 1

print(ans)