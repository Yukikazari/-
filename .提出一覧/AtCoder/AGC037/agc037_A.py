S = input()

res = 0
tmp = ""
last = ""

for s in S:
    tmp += s
    if tmp == last:
        continue

    last = tmp
    tmp = ""
    res += 1

print(res)