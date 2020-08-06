N, M = map(int, input().split())
PS = [list(input().split()) for _ in range(M)]

acdic = {}

wadic = [0] * 10 ** 5

ac = 0
wa = 0

for ps in PS:
    p = int(ps[0])
    s = ps[1]

    if not p in acdic:
        if s == "WA":
            wadic[p] += 1
        else:
            ac += 1
            acdic[p] = True
            wa += wadic[p]


print(ac, wa)