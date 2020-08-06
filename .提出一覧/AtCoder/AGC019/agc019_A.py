Q, H, S, D = map(int, input().split())
N = float(input())

N = int(N * 4)

q = Q * 8
h = H * 4
s = S * 2
d = D

res = 0

while N > 0:
    if q > d and h > d and s > d:
        res += N // 8 * D
        N %= 8
        d = 10 ** 9
        
    elif q > s and h > s:
        res += N // 4 * S
        N %= 4
        s = 10 ** 9
        
    elif q > h:
        res += N // 2 * H
        N %= 2
        h = 10 ** 9

    else:
        res += N * Q
        N = 0

print(res)