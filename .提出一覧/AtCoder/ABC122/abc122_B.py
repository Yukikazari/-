S = list(input())

acgt = ["A", "C", "G", "T"]

res = 0

t = 0

for s in S:
    if s in acgt:
        t += 1
    else:
        res = max(res, t)
        t = 0

res = max(res, t)

print(res)