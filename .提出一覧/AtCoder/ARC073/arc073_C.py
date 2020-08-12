N, T = map(int, input().split())
TL = list(map(int, input().split()))

ans = T

for i in range(1, N):
    if TL[i] - TL[i - 1] > T:
        ans += T
    else:
        ans += TL[i] - TL[i - 1]

print(ans)