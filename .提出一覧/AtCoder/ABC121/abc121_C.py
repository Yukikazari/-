N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

money = 0

m = 0
for ab in AB:
    a = ab[0]
    b = ab[1]

    if m + b <= M:
        money += a * b
        m += b
    
    else:
        money += min(b, (M - m)) * a
        m += min(b, (M - m))

    if m == M:
        break

print(money)