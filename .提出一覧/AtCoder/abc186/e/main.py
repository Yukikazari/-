#!/usr/bin/env python3

#import
#import math
#import numpy as np
T = int(input())

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

for _ in range(T):
    N, S, K = map(int, input().split())

    now = N - S
    if now % K == 0:
        print(now // K)

    else:
        gcd, x, y = egcd(N, K)

        if now % gcd != 0:
            print(-1)

        else:
            t1 = 
