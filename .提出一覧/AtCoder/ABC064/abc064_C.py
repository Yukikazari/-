N = int(input())
A = list(map(int, input().split()))

free = 0
colors = {}

for a in A:
    if a < 3200:
        ai = a // 400
        colors[ai] = True

    else:
        free += 1

lc = len(colors)

print(max(1, lc), lc + free)
