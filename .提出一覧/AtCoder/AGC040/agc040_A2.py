S = list(input())
ls = len(S)

a = [0] * (len(S) + 1)

for i in range(ls):
    if S[i] == "<":
        a[i + 1] = max(a[i + 1], a[i] + 1)
        
for i in range(ls - 1, -1, -1):
    if S[i] == ">":
        a[i] = max(a[i], a[i + 1] + 1)
        
print(sum(a))