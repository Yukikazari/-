#import
import math
#import numpy as np
#= int(input())
#= input()
N, D = map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
XY = [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

res = 0

for xy in XY:
    x = xy[0]
    y = xy[1]

    kyori = math.sqrt(x ** 2 + y ** 2)
    
    if kyori <= D:
        res += 1


print(res)