import math

A, B = map(int, input().split())

for i in range(10, 2000):
    a = math.floor(i * 0.08)
    b = math.floor(i * 0.1)
    if a == A and b == B:
        print(i)
        exit()

print(-1)