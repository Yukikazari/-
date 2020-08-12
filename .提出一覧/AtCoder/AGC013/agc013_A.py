N = int(input())
A = list(map(int, input().split()))

ans = 0

up = None

for i in range(1, N):
    if up == None:
        if not A[i] == A[i - 1]:
            up = A[i] > A[i - 1]
            
    elif up:
        if A[i] < A[i - 1]:
            ans += 1
            up = None

    else:
        if A[i] > A[i - 1]:
            ans += 1
            up = None

print(ans + 1)