#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    dpMAX = 10**9
    abc = "abcdefghijklmnopqrstuvwxyz"

    abcdic = {i:[] for i in range(1, 27)}
    dp = [[dpMAX] * W for _ in range(H)]
    warp = [[0] * W for _ in range(H)]
    seen = [False] * (H * W)

    G = 0
    Gh = 0; Gw = 0

    que = []

    for i in range(H):
        for j in range(W):
            if A[i][j] == "S":
                que.append(i * W + j)
                dp[i][j] = 0
                seen[i * W + j] = True
            elif A[i][j] == "G":
                Gh = i
                Gw = j
                G = i * W + j
            elif A[i][j] in abc:
                t = abc.find(A[i][j]) + 1
                abcdic[t].append(i * W + j)
                warp[i][j] = t
            elif A[i][j] == "#":
                warp[i][j] = -1

    while len(que):
        q = que.pop(0)
        h = q // W
        w = q % W

        if warp[h][w]:
            for a in abcdic[warp[h][w]]:
                hh = a // W
                ww = a % W

                warp[hh][ww] = 0
                if seen[a]:
                    continue

                que.append(a)
                dp[hh][ww] = min(dp[hh][ww], dp[h][w] + 1)
                seen[a] = True

        if 0 <= h - 1:
            if warp[h - 1][w] != -1:
                if not seen[(h - 1) * W + w]:
                    que.append((h - 1) * W + w)
                    dp[h - 1][w] = dp[h][w] + 1
                    seen[(h - 1) * W + w] = True
        if h + 1 < H:
            if warp[h + 1][w] != -1:
                if not seen[(h + 1) * W + w]:
                    que.append((h + 1) * W + w)
                    dp[h + 1][w] = dp[h][w] + 1
                    seen[(h + 1) * W + w] = True
        if 0 <= w - 1:
            if warp[h][w - 1] != -1:
                if not seen[(h) * W + w - 1]:
                    que.append((h) * W + w - 1)
                    dp[h][w - 1] = dp[h][w] + 1
                    seen[(h) * W + w - 1] = True
        if w + 1 < W:
            if warp[h][w + 1] != -1:
                if not seen[(h) * W + w + 1]:
                    que.append((h) * W + w + 1)
                    dp[h][w + 1] = dp[h][w] + 1
                    seen[(h) * W + w + 1] = True

    print(dp[Gh][Gw] if seen[G] else - 1)

main()

# print(warp)
