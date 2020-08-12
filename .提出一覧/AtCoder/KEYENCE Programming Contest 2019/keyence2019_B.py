S = input()

key = "keyence"

t = -1

for i in range(7):
    if not S[i] == key[i]:
        t = i
        break

if t == -1:
    t = 7

for i in range(1, 8):
    if not S[-i] == key[-i]:
        t += i - 1
        break

if t >= 7:
    print("YES")
else:
    print("NO")

