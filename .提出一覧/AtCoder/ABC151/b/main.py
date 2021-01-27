#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

Asum = sum(A)

print(max(0, N * M - Asum) if N * M - Asum <= K else -1)
