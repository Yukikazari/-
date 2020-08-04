A, B, C, K = map(int, input().split())

# 1回後 A:B+C B:A+C C:A+B   A-B = B-A
# 2回後 A:2A+B+C B:A+2B+C C:A+B+2C    A-B = A-B

if K % 2 == 0:
    print(A - B)
else:
    print(B - A)
    