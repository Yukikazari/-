N = int(input())

A = [int(input()) for _ in range(N)]

nextint = A[0]

for i in range(1, N + 1):
    if nextint == 2:
        print(i)
        exit()

    nextint = A[nextint - 1]

print(-1)