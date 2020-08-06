N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

#  典型経路探索なのでDP、進研ゼミで習った

dp = [[0] * N for _ in range(2)]

for i in range(2):
    for j in range(N):
        if i == 0 and j == 0:
            dp[i][j] = A[0][0]

        elif i == 0:
            dp[i][j] = dp[i][j - 1] + A[i][j]

        elif j == 0:
            dp[i][j] = dp[i - 1][j] + A[i][j]
            
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + A[i][j]
            
print(dp[1][N - 1])