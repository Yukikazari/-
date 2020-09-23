import sys
sys.setrecursionlimit(10 ** 7)

H,W= map(int, input().split())
C = list(map(int, input().split()))
D= list(map(int, input().split()))
S = [list(input()) for _ in range(H)]

def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    res = 10**9
    ist = i - min(2, i)
    ien = i + min(3, H - i)
    jst = j - min(2, j)
    jen = j + min(3, W - i)


    for ii in range(ist, ien):
        for jj in range(jst, jen):
            if ii != 0 and jj != 0:
                if (abs(ii) == 1 and j == 0) or abs(jj) == 1 and i == 0:
                    if S[ii][jj] == ".":
                        res = min(res, dfs(ii, jj))

                else:
                    if S[ii][jj] == ".":
                        res = min(res, dfs(ii, jj) + 1) 

    dp[i][j] = res
    return res

dp = [[-1] * W for _ in range(H)]

dp[D[0] - 1][D[1] - 1] = 0

dfs(C[0] - 1, C[1] - 1)

print(dp[C[0] - 1][C[1] - 1])
print(dp)
