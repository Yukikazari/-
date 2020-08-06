N = int(input())
A = list(map(int, input().split()))

res = 0

for i in range(N):
    while A[i] % 2 == 0:
        A[i] /= 2
        res += 1

print(res)