K, N = map(int, input().split())
A = list(map(int, input().split()))

maxlange = K - A[-1] + A[0]

for i in range(1, N):
    maxlange = max(maxlange, A[i] - A[i - 1])
    
print(K - maxlange)
