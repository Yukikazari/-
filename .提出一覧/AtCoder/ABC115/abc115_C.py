N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]

#  hi <= 10**9なのにresの最小値10**7にしたせいでガバるのアホすぎないか？

H.sort()

res = H[-1] - H[0]

for i in range(N - K + 1):
    t1 = H[i]
    t2 = H[i + K - 1]
    res = min(res, abs(t2 - t1))

print(res)