#!/usr/bin/env python3

N, M = map(int, input().split())
S = input()
T = input()

def gcd(x, y):
    if x < y:
        x, y = y, x

    if y == 0:
        return x

    else:
        return gcd(y, x % y)

nm = gcd(N, M)

if nm == 1:
    if S[0] == T[0]:
        print(N * M)
    else:
        print(-1)

else:
    sp = N // nm
    tp = M // nm

    si = 0
    ti = 0

    ans = True

    while (si < N and ti < M):
        if S[si] == T[ti]:
            si += sp
            ti += tp
        else:
            ans = False
            break

    if ans:
        print(N * M // nm)
    else:
        print(-1)