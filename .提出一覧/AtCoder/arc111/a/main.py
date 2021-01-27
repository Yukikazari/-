#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

t = pow(10, N, M ** 2)

print(t // M % M)
