#import
#import math
#import numpy as np
#= int(input())
#= input()
a, b, c, d = map(int, input().split())

print(max(a *c, b * d, a * d, b * c))