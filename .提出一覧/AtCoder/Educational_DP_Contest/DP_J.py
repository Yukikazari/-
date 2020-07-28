import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
a = list(map(int, input().split()))

one = a.count(1)
two = a.count(2)
three = a.count(3)

dp = [[[-1] * 301 for _ in range(301)] for _ in range(301)]

def rec(i, j, k):
    if dp[i][j][k] >= 0:
        return dp[i][j][k]

    if i == 0 and j == 0 and k == 0:
        return 0.0

    res = 0.0

    if i > 0:
        res += rec(i - 1, j, k) * i
    if j > 0:
        res += rec(i + 1, j - 1, k) * j
    if k > 0:
        res += rec(i, j + 1, k - 1) * k
        
    res += N

    res /= i + j + k

    dp[i][j][k] = res
    return res

res = rec(one, two, three)

print(res)
