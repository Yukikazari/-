#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
W.sort()

t = 0
for i in range(1, N // 2 + 1):
    t += H[i * 2] - H[i * 2 - 1]

h = [0] * N
h[0] = t

for i in range(1, N):
    if i % 2 == 1:
        h[i] = h[i - 1] + H[i] - H[i - 1]
    else:
        h[i] = h[i - 1] + H[i - 1] - H[i]
        
def is_ok(arg, t):
    return W[arg] < t

def meguru_bisect(ok, ng, t):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, t):
            ok = mid
        else:
            ng = mid
    return ok

ans = 10 ** 20

for i in range(N):
    tmp = meguru_bisect(0, M, H[i])
    if tmp > 0 and abs(H[i] - W[tmp]) > abs(H[i] - W[tmp - 1]):
        tmp -= 1
    if tmp < M - 1 and abs(H[i] - W[tmp]) > abs(H[i] - W[tmp + 1]):
        tmp += 1

    ans = min(ans, h[i] + abs(H[i] - W[tmp]))

print(ans)