N = int(input())
S = input()

li1 = [0] * 26
li2 = [0] * 26

ans = 0

for s in S:
    si = ord(s) - 97
    li1[si] += 1

for s in S:
    si = ord(s) - 97
    li2[si] += 1
    li1[si] -= 1

    t = 0
    for i in range(26):
        if li1[i] > 0 and li2[i] > 0:
            t += 1

    ans = max(ans, t)

print(ans)