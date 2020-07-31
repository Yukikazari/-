N, K = [int(input()), int(input())]

X= list(map(int, input().split()))

res = 0

for x in X:
    res += min(x, K - x) * 2

print(res)