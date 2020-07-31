N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

d = D - 1

eat = 0
for a in A:
    eat += d // a + 1

print(eat + X)