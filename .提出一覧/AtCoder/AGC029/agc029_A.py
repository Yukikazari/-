import math

S = list(input())

t = 0

res = 0

for i in range(len(S)):
    if S[i] == "W":
        res += i - t
        t += 1

if len(S) == 1:
    print(0)

elif S.count("B") == 1 and S[-1] == "B":
    print(0)

else:
    print(res)