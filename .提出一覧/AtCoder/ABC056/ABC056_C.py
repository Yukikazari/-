import math

X = int(input())

x = max(0, int(math.sqrt(X)) - 10)

while True:
    xx = x * (x + 1) // 2
    if X <= xx:
        print(x)
        exit()
    else:
        x += 1