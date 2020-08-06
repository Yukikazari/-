import math

N = int(input())

t1 = 1

for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        t1 = i

t2 = N // t1

print(t1 + t2 - 2)