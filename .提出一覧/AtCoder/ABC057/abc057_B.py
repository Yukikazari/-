N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

for ab in AB:
    a = ab[0]
    b = ab[1]

    mr = 10 ** 9
    cp = 1

    for i, cd in enumerate(CD, 1):
        c = cd[0]
        d = cd[1]

        l = abs(a-c) + abs(b-d)

        if l < mr:
            mr = l
            cp = i

    print(cp)