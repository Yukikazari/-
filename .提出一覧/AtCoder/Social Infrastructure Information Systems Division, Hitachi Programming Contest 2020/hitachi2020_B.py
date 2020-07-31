A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

xyc= [list(map(int, input().split())) for _ in range(M)]

minmoney = min(a) + min(b)

for obj in xyc:
    summoney = a[obj[0] - 1] + b[obj[1] - 1] - obj[2]
    minmoney = min(minmoney, summoney)

print(minmoney)