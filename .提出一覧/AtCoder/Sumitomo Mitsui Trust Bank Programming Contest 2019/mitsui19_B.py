import math

N = int(input())

n = N / (1.08)

n0 = math.floor(n) - 1
n1 = math.floor(n)
n2 = math.ceil(n)

if int(n0 * 1.08) == N:
    print(n0)
elif int(n1 * 1.08) == N:
    print(n1)
elif int(n2 * 1.08) == N:
    print(n2)
else:
    print(":(")