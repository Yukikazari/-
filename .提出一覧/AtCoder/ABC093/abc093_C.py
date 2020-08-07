A = list(map(int, input().split()))

A.sort()

t1 = A[2] - A[1]
t2 = A[1] - A[0]

if t2 % 2 == 0:
    print(t1 + t2 // 2)

else:
    print(t1 + t2 // 2 + 2)