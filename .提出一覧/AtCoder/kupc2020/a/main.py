N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(1, N):
    ans += abs(xy[i][0] - xy[i - 1][0]) + abs(xy[i][1] - xy[i - 1][1])
    
    
print(ans)