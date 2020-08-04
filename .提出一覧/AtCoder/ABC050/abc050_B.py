N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]

tsum = sum(T)

for px in PX:
    p = px[0]
    x = px[1]

    t = tsum - T[p - 1] + x
    print(t)
