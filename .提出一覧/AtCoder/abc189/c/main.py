#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

dic = {i:[] for i in range(1, 10 ** 5 + 1)}

for i in range(N):
    dic[A[i]].append(i)

ans = 0
li = []

for i in range(10 ** 5, 0, -1):
    if dic[i]:
        for j in dic[i]:
            li.append(j)

        li.sort()

        cnt = 0
        for j in range(len(li)):
            if j == 0:
                cnt += 1
            else:
                if li[j] - li[j - 1] == 1:
                    cnt += 1
                else:
                    ans = max(ans, cnt * i)
                    cnt = 1

        # print(li)  
        ans = max(ans, cnt * i)

print(ans)

