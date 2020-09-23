N = int(input())
A = list(map(int, input().split()))

maxtall = A[0]
ans = 0
for i in range(1, N):
    if A[i] < maxtall:
        ans += maxtall - A[i]

    elif A[i] > maxtall:
        maxtall = A[i]

print(ans)