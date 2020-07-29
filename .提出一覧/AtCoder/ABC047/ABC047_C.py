S = input()

s = S[0]

r = 0

for i in range(1, len(S)):
    if s != S[i]:
        r += 1

    s = S[i]

print(r)