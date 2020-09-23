#import
import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Adic = {}
Bdic = {}

for a in A:
    if a in Adic:
        Adic[a] += 1
    else:
        Adic[a] = 1

for b in B:
    if b in Bdic:
        Bdic[b] += 1
    else:
        Bdic[b] = 1

isok = True

maxb = 0
for b in Bdic:
    if b in Adic:
        t = Adic[b]
    else:
        t = 0

    if Bdic[b] + t > N:
        isok = False
        break

    if maxb < Bdic[b]:
        maxb = Bdic[b]

if not isok:
    print("No")
    exit()

print("Yes")

for i in range(N):
    print(B[-maxb + i], end="")

    if i != N-1:
        print(" ", end="")

print()
