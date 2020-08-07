import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

count = N * (N - 1) // 2
t = 0.0

for i in range(N):
    for j in range(i + 1, N):
        x1 = XY[i][0]
        y1 = XY[i][1]
        x2 = XY[j][0]
        y2 = XY[j][1]

        t += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(t / count * (N - 1))