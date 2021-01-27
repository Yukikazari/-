#!/usr/bin/env python3

#import
import math
#import numpy as np
#= int(input())
#= input()
S, P = map(int, input().split())

def is_ok(N):
    M = S - N
    return N * M <= P

def meguru_bisect(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = meguru_bisect(1, S // 2 + 1)

if ans * (S - ans) == P:
    print("Yes")
else:
    print("No")
