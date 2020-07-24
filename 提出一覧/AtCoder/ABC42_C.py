N, K = map(int, input().split())

D = list(map(str, input().split()))

while True:
    n = str(N)
    nn = str(N)

    for o in nn:
        if o in D:
            N += 1
            nn = str(N)
            break

    if n == nn:
        break

print(N)