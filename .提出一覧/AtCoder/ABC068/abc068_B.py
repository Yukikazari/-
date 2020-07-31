N = int(input())

n = 1

for _ in range(N):
    n *= 2
    if n > N:
        print(n // 2)
        exit()