X, N = map(int, input().split())

if N != 0:
    p = list(map(int, input().split()))
else:
    p = []

for i in range(100):
    if (X - i) not in p:
        print(X - i)
        break

    elif (X + i) not in p:
        print(X + i)
        break

