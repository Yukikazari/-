N = int(input())
v = list(map(int, input().split()))

while len(v) > 1:
    v.sort()
    t1 = v.pop(0)
    t2 = v.pop(0)

    v.append((t1 + t2) / 2)

print(v[0])