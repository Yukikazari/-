N = int(input())
L = list(map(int, input().split()))
ans = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            maxint = max(L[i],  L[j],  L[k])
            sumint = L[i] + L[j] + L[k]
            if sumint > 2 * maxint:
                if L[i] != L[j] and L[j] != L[k] and L[i] != L[k] :
                    ans += 1

print(ans)