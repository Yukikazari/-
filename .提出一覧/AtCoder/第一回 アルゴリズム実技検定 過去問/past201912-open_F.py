S = input()

data = []
start = 0
for i in range(1, len(S)):
    if i == start:
        continue
    if S[i].isupper():
        data.append(S[start:i + 1])
        start = i + 1

data.sort(key=str.lower)

ans = "".join(data)
print(ans)