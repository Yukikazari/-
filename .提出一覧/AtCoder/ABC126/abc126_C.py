N, K = map(int, input().split())

ans = 0.0

for i in range(1, N + 1):
    num = i
    t = 0
    while num < K:
        t += 1
        num *= 2

    ans += 1 / 2 ** t
    
print(ans / N)