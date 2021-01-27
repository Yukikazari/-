#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = input()
T = S[::-1]
N = len(S)

ans = True

for i in range(N//2+1):
    if S[i] != T[i]:
        ans = False

s = S[:(N - 1) // 2]
t = s[::-1]

for i in range(len(s)):
    if s[i] != t[i]:
        ans = False

s = S[(N + 3) // 2 - 1:]
t = s[::-1]

for i in range(len(s)):
    if s[i] != t[i]:
        ans = False

if ans:
    print("Yes")

else:
    print("No")
 
