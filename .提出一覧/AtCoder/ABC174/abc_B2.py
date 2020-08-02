N, D = map(int, input().split())

XY = [list(map(int, input().split())) for _ in range(N)]

res = 0

for xy in XY:
    x = xy[0]
    y = xy[1]
    
    if x ** 2 + y ** 2 <= D ** 2:
        res += 1

print(res)