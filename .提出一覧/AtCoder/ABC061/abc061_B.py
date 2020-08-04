N, M = map(int, input().split())

r = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    r[a - 1] += 1
    r[b - 1] += 1
    
for rr in r:
    print(rr)