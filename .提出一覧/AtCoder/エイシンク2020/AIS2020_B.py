N = int(input())
a = list(map(int, input().split()))

c = 0

for i in range(N):
    if i % 2 == 0:
        if a[i] % 2 == 1:
            c += 1

print(c)