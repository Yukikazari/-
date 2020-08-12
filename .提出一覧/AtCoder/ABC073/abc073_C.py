N = int(input())
A = [int(input()) for _ in range(N)]

dic = {}

for a in A:
    if a in dic:
        dic[a] += 1

    else:
        dic[a] = 1

ans = 0

for a in dic:
    if dic[a] % 2 != 0:
        ans += 1

print(ans)