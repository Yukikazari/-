import math

abc = [int(input()) for _ in range(5)]

s = 0
t = 0

for a in abc:
    s += math.ceil(a / 10)
    if a % 10 != 0:
        t = max(t, 10 - a % 10)
        
if t != 0:
    print(s * 10 - t)
else:
    print(s * 10)
