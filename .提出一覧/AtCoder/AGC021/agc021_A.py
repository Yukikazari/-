N = int(input())

n = str(N)

res = 0

if len(n) == 1:
    res = N

else:
    nine = True
    for i in range(1, len(n)):
        if n[i] != "9":
            nine = False
            break

    if nine:
        res = int(n[0]) + 9 * (len(n) - 1)
    else:
        res = (int(n[0]) - 1) + 9 * (len(n) - 1)

print(res)