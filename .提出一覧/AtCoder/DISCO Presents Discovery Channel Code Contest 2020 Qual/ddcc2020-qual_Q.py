N = int(input())
A = list(map(int, input().split()))

sumA = sum(A)
half = sumA / 2

r = 0.0

t1 = 0.0
t2 = 0.0
for a in A:
    t2 = t1
    t1 += a

    if t1 >= half:
        r = min(abs(half - t1), abs(half - t2))
        break

print(int(r * 2))