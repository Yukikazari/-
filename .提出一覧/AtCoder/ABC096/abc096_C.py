H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = True

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            t = False
            if i != 0:
                t = max(t, S[i - 1][j] == "#")
            if i != H - 1:
                t = max(t, S[i + 1][j] == "#")
            if j != 0:
                t = max(t, S[i][j - 1] == "#")
            if j != W - 1:
                t = max(t, S[i][j + 1] == "#")

            if not t:
                ans = False
                break

if ans:
    print("Yes")

else:
    print("No")
