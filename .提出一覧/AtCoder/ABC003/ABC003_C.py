N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort()

res = 0

for i in range(N - K, N):
    res = (res + R[i]) / 2

print(res)