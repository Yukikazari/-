N = int(input())

A = list(map(int, input().split()))

res = 10 ** 9

for a in A:
    t = 0
    while a % 2 == 0:
        t += 1
        a //= 2

    res = min(res, t)

print(res)