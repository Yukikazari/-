N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0

for i in range(N - 1, -1, -1):
    if A[i + 1] > 0:
        if A[i + 1] > B[i]:
            res += B[i]
            B[i] = 0
        else:
            res += A[i + 1]
            B[i] -= A[i + 1]

    if B[i] > 0 and A[i] > 0:
        if B[i] > A[i]:
            res += A[i]
            A[i] = 0
        else:
            res += B[i]
            A[i] -= B[i]

print(res)