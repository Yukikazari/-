N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]

li = [-1] * N

for s, c in SC:
    if li[s - 1] == -1:
        li[s - 1] = c
    else:
        if not li[s - 1] == c:
            print(-1)
            exit()

ans = ""

if N == 1:
    print(max(0, li[0]))
    exit()

for i in range(N):
    if i == 0:
        if li[i] == 0:
            print(-1)
            exit()
        else:
            ans += str(max(li[i], 1))

    else:
        ans += str(max(0, li[i]))

print(ans)