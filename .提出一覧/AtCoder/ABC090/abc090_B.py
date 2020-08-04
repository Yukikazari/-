A, B = map(int, input().split())

res = 0

for i in range(100, 1000):
    s = str(i)
    t = s + s[1] + s[0]
    ti = int(t)
    if ti >= A and ti <= B:
        res += 1

print(res)