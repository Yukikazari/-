N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0

for i in range(N):
    ans += A[N + 2 * i]

print(ans)