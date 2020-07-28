
def mod(num):
    return num % (10 ** 9 + 7)

H, W = map(int, input().split())
dp = [[0] * W for _ in range(H)]

for i in range(H):
    a = input()
    for j in range(W):
        if a[j] == "#":
            dp[i][j] = -1

dp[0][0] = 1

for col in range(1, W):
    if dp[0][col] != -1:
        dp[0][col] = dp[0][col - 1]
    else:
        dp[0][col] = 0

for row in range(1, H):
    for col in range(W):
        if dp[row][col] != -1:
            if col == 0:
                dp[row][col] = dp[row - 1][col]
            else:
                dp[row][col] = mod(dp[row - 1][col] + dp[row][col - 1])
        else:
            dp[row][col] = 0

print(dp[-1][-1])