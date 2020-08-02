N = int(input())

c = list(map(str, input()))

r = c.count("R")
w = 0

res = max(r, w)

for i in range(N):
    if c[i] == "R":
        r -= 1
    else:
        w += 1

    now = max(r, w)
    res = min(res, now)

print(res)