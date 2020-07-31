N, M, C= map(int, input().split())
B = list(map(int, input().split()))

res = 0
c = -C

for _ in range(N):
    A = list(map(int, input().split()))
    t = 0
    for i in range(M):
        t += A[i] * B[i]

    if t > c:
        res += 1

print(res)