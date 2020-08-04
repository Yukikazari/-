import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

res = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        t = 0
        for d in range(D):
            t += (X[i][d] - X[j][d]) ** 2

        tt = math.sqrt(t)
        if tt.is_integer():
            res += 1

print(res)