N = int(input())
A = list(map(int, input().split()))

odd = 0

for a in A:
    if a % 2 == 1:
        odd += 1


print(3 ** N - 2 ** (N - odd))
