N = int(input())
d = list(map(int, input().split()))

d.sort()

n = N // 2

t1 = d[n - 1]
t2 = d[n]

print(t2 - t1)