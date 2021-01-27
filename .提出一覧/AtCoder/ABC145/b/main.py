#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
S = input()

if len(S) % 2 == 0 and S[: len(S) // 2] == S[len(S) // 2 :]:
    print("Yes")
else:
    print("No")