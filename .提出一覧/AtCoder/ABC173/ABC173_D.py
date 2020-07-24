N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

res = 0

res += A.pop(0)

count = 1

for i in range(N // 2):
    for _ in range(2):
        if count < N - 1:
            res += A[i]
            count += 1

print(res)