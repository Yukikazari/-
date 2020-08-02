N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

res = [0] * N

for a in A:
    res[a - 1] += 1
    
for i in range(N):
    if K - Q + res[i] > 0:
        print("Yes")
    else:
        print("No")