import copy

N = int(input())
A = [int(input()) for _ in range(N)]

aa = copy.deepcopy(A)
aa.sort()

first = aa[-1]
second = aa[-2]

for a in A:
    if a == first:
        print(second)
    else:
        print(first)
