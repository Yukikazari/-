import math

X = int(input())

num = [True] * (X * 2 + 1)

t = min(X * 2 + 1, int(math.sqrt(X) + 10))

for i in range(2, t):
    if num[i]:
        for j in range(2, (X * 2) // i):
            num[i * j] = False

for i in range(X, X * 2):
    if num[i]:
        print(i)
        exit()