N = int(input())
SP = []

for i in range(1, N + 1):
    s, p = input().split()
    sp = [s, int(p), i]
    SP.append(sp)

SP.sort(key=lambda x: x[1], reverse=True)
SP.sort(key=lambda x: x[0])

for s in SP:
    print(s[2])