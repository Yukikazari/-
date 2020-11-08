#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, K = map(int, input().split())

snuke = [False] * N

for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))

    for a in A:
        snuke[a - 1] = True

print(snuke.count(False))