N, K, S = map(int, input().split())

ans = []

for _ in range(K):
    ans.append(str(S))

for _ in range(N - K):
    ans.append(str(abs(S - 10**9 + 1)))

print(" ".join(ans))