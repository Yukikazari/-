A, B, C = map(int, input().split())

cnt = 0

last = [A, B, C]

while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    a = A // 2
    b = B // 2
    c = C // 2
    cnt += 1
    A = b + c
    B = a + c
    C = a + b
    if A in last and B in last and C in last:
        print(-1)
        exit()

    last = [A, B, C]

print(cnt)

