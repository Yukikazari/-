import numpy as np
import math

N = int(input())

a = list(map(int, input().split()))

avr = np.average(a)

av1 = math.floor(avr)
av2 = math.ceil(avr)

res1 = 0
res2 = 0

for num in a:
    res1 += (num - av1) ** 2
    res2 += (num - av2) ** 2

print(min(res1, res2))