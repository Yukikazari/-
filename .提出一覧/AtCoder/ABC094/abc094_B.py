N, M, X= map(int, input().split())
A = list(map(int, input().split()))

res1 = 0
res2 = 0

for a in A:
    if a < X:
        res1 += 1
    else:
        res2 += 1

print(min(res1, res2))