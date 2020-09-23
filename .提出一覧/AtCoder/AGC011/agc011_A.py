N, C, K= map(int, input().split())
T = [int(input()) for _ in range(N)]

T.sort()

ans = 0

cnt = 0
last = T[0] + K

for t in T:
    if cnt < C and last >= t:
        cnt += 1
    else:
        ans += 1
        cnt = 1
        last = t + K

if cnt > 0:
    ans += 1

print(ans)