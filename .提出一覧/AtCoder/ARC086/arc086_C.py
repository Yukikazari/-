N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = {}

for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

li = [0] * (N + 1)

#  li[i] = j  i:ボールの数 j:種類

for a in dic:
    li[dic[a]] += 1

ans = 0
k = len(dic)

for i in range(N):
    if li[i] > 0:
        if k - li[i] >= K:
            ans += i * li[i]
            k -= li[i]
        else:
            ans += i * (k - K)
            k -= li[i]

    if k <= K:
        break

print(ans)