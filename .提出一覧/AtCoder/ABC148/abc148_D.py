N = int(input())
A = list(map(int, input().split()))

num = 1

res = 0

for a in A:
    if a == num:
        num += 1
    else:
        res += 1


if res == N:
    print(-1)
else:
    print(res)