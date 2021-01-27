#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
N = input()

dic = {i: 0 for i in range(3)}

for n in N:
    nn = int(n)
    dic[nn % 3] += 1

t = (dic[1] + dic[2] * 2) % 3
if t == 0:
    print(0)
elif len(N) > 1 and t == 1 and dic[1] > 0:
    print(1)
elif len(N) > 1 and t == 2 and dic[2] > 0:
    print(1)
elif len(N) > 2 and t == 2 and dic[1] > 1:
    print(2)
elif len(N) > 2 and t == 1 and dic[2] > 1:
    print(2)
else:
    print(-1)