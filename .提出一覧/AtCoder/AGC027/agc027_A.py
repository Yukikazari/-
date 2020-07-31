N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

res = 0

for aa in a:
    x -= aa
    if x < 0:
        print(res)
        exit()
    res += 1

if x == 0:
    print(N)
else:
    print(N - 1)