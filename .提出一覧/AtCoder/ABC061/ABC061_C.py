N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x: x[0])

cnt = 0

for ab in A:
    a = ab[0]
    b = ab[1]

    cnt += b
    if cnt >= K:
        print(a)
        exit()