N = int(input())
A = list(map(int, input().split()))

a = [0] * N

for i in range(N):
    a[A[i] - 1] = str(i + 1)

res = " ".join(a)

print(res)