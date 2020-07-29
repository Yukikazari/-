W, H, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

xmin = 0
xmax = W
ymin = 0
ymax = H

for obj in A:
    x = obj[0]
    y = obj[1]
    a = obj[2]

    if a == 1:
        xmin = max(x, xmin)
    elif a == 2:
        xmax = min(x, xmax)
    elif a == 3:
        ymin = max(y, ymin)
    elif a == 4:
        ymax = min(y, ymax)

x = xmax - xmin
y = ymax - ymin

if x > 0 and y > 0:
    print(x * y)
else:
    print(0)