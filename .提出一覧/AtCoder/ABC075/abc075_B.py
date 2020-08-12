H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] != "#":
            s = 0

            ist = -1
            ien = 2
            jst = -1
            jen = 2

            if h == 0:
                ist = 0
            if h == H - 1:
                ien = 1
            if w == 0:
                jst = 0
            if w == W - 1:
                jen = 1

            for i in range(ist, ien):
                for j in range(jst, jen):
                    if S[h + i][w + j] == "#":
                        s += 1

            S[h][w] = str(s)

for s in S:
    st = "".join(s)
    print(st)