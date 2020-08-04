N = int(input())
H = list(map(int, input().split()))

res = 0
t = 0
for i in range(N - 1):
    if H[i + 1] <= H[i]:
        t += 1
    else:
        res = max(res, t)
        t = 0

res = max(res, t)
print(res)