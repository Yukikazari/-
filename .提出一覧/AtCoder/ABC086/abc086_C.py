N = int(input())
TXY = [list(map(int, input().split())) for _ in range(N)]

ans = True

for i in range(N):
    if i == 0:
        t = TXY[i][0]
        x = TXY[i][1]
        y = TXY[i][2]

    else:
        t = TXY[i][0] - TXY[i - 1][0]
        x = abs(TXY[i][1] - TXY[i - 1][1])
        y = abs(TXY[i][2] - TXY[i - 1][2])

    xy = x + y
    if t == xy or (t > xy and (t - xy) % 2 == 0):
        pass
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")