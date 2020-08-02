N = int(input())
S = input()

res = 0
t = 0

for s in S:
    if s == "I":
        t += 1
    else:
        t -= 1

    res = max(res, t)

print(res)