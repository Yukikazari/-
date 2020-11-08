#!/usr/bin/env python3

#import
import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
X = list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

ans = [0] * 3

for x in X:
    ans[0] += abs(x)
    ans[1] += x ** 2
    ans[2] = max(ans[2], abs(x))

print(ans[0])
print(math.sqrt(ans[1]))
print(ans[2])
