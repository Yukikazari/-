#!/usr/bin/env python3

#import
#import math
#import numpy as np
T = int(input())
#= input()
#= map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

for _ in range(T):
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    if (N - M - 2) % 2 == 1:
        print("First")
    else:
        print("Second")
