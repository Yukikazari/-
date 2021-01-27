#!/usr/bin/env python3

X, Y = map(int, input().split())

li = [0] * (10 ** 6)
li[0] = 1
for i in range(1, 10 ** 6):
    li[i] = li[i - 1] * i
    li[i] %= 10 ** 9 + 7

if (X + Y) % 3 != 0:
    print(0)
else:
    m = (X + Y) // 3
    for i in range(m + 1):
        n = m - i
        if X == (n + 2 * i) and Y == (2 * n + i):
            print((li[m] * pow(li[m - i], -1, 10 ** 9 + 7) * pow(li[i], -1, 10 ** 9 + 7)) % (10 ** 9 + 7))
            # print(n, i)
            exit()

    print(0)
