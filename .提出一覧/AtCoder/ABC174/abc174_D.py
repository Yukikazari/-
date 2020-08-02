#import
#import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
c = list(map(str, input()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

whitec = c.count("W")

res = 0

for i in range(N - whitec, N):
    if c[i] == "R":
        res += 1

print(res)