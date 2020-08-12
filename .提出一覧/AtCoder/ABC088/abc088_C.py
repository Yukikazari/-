C = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    minint = min(C[i])
    for j in range(3):
        C[i][j] -= minint

ans = True

for j in range(3):
    t = C[0][j]
    for i in range(3):
        if t != C[i][j]:
            ans = False
            break

if ans:
    print("Yes")
else:
    print("No")