N, K = map(int, input().split())
P = list(map(int, input().split()))

a = [0] * (N - K + 1)
a[0] = sum(P[:K])
for i in range(1, N - K + 1):
    a[i] = a[i - 1] - P[i - 1] + P[i + K - 1]
    
print((max(a) + K) / 2)