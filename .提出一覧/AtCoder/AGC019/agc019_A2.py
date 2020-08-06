Q, H, S, D = map(int, input().split())
N = int(input())

H = min(H, Q * 2)
S = min(S, H * 2)

if S * 2 < D:
    print(N * S)

else:
    print((N // 2) * D + (N % 2) * S)