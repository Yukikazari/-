N, L = map(int, input().split())

S = []

for _ in range(N):
    s = input()
    S.append(s)

S.sort()

for obj in S:
    print(obj, end="")

print()