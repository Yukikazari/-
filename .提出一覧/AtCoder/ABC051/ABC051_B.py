K, S = map(int, input().split())

r = 0

for i in range(K + 1):
    for j in range(K + 1):
        z = S - (i + j)
        if z >= 0 and z <= K:
            r += 1

print(r)