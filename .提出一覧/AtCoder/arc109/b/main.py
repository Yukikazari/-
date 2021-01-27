#!/usr/bin/env python3

#import
#import math
#import numpy as np
n = int(input())

def is_ok(arg):
    return arg * (arg + 1) // 2 <= n + 1

def meguru_bisect(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

t = meguru_bisect(1, n + 1)

print(n - t + 1)