N, A, B = map(int, input().split())

r = [0] * 40

for i in range(1, N + 1):
    si = str(i)
    t = 0
    for j in range(len(si)):
        t += int(si[j])

    r[t] += i

res = 0

for i in range(A, B + 1):
    res += r[i]

print(res)