#!/usr/bin/env python3

#import
#import math
#import numpy as np
K = int(input())
ans = [i for i in range(1, 10)]

now = 0
while len(ans) < K + 10:
    if ans[now] % 10 != 0:
        ans.append(ans[now] * 10 + ans[now] % 10 - 1)
    ans.append(ans[now] * 10 + ans[now] % 10)
    if ans[now] % 10 != 9:
        ans.append(ans[now] * 10 + ans[now] % 10 + 1)
    now += 1

print(ans[K - 1])