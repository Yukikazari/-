S = input()

st = 0
en = 0

for i in range(len(S)):
    if S[i] == "A":
        st = i
        break

for i in range(len(S)):
    if S[i] == "Z":
        en = i

print(en - st + 1)