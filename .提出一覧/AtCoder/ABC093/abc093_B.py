A, B, K = map(int, input().split())

r = []

for i in range(A, min(A + K, B)):
    print(i)
    r.append(i)

for i in range(max(A, B - K + 1), B + 1):
    if not i in r:
        print(i)