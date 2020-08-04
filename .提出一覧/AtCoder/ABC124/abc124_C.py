S = input()

res1 = 0
res2 = 0

for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "0":
            res1 += 1
        else:
            res2 += 1
    else:
        if S[i] == "1":
            res1 += 1
        else:
            res2 += 1

print(min(res1, res2))