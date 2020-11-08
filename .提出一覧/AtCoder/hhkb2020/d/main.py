#!/usr/bin/env python3

#import
#import math
#import numpy as np
T = int(input())


for _ in range(T):
    N, A, B = map(int, input().split())

    a = N - A + 1
    b = N - B + 1
    n = max(0, N - (A + B))
    print((max(0, (b ** 2 - A ** 2) * 4) + max(0, (n * (n + 1) // 2) * A * 4) + (a - B) * b * 4 + max(0, (n * (n + 1) // 2) ** 2 * 4 )) % (10 ** 9 + 7))