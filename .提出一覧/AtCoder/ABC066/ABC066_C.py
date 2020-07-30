n = int(input())
a = list(map(int, input().split()))

a1 = []
a2 = []

for i in range(n):
    if i % 2 == 0:
        a2.append(a[i])
    else:
        a1.append(a[i])


if n % 2 != 0:
    #  偶数
    a2.reverse()
    res = a2 + a1

else:
    #  奇数
    a1.reverse()
    res = a1 + a2

[print(x, end=" ") for x in res]
print()