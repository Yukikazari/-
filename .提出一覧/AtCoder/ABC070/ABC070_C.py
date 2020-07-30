N = int(input())
T = [int(input()) for _ in range(N)]


def gcd(x, y):
    if x < y:
        t = x
        x = y
        y = t

    if y == 0:
        return x

    else:
        return gcd(y, x % y)


if N == 1:
    print(T[0])
    exit()

res = T[0] * T[1] // gcd(T[0], T[1])

if N > 2:
    for i in range(2, N):
        r = res * T[i] // gcd(res, T[i])
        res = max(r, res)

print(res)