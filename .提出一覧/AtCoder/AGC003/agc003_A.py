S = list(input())

res = True

n = S.count("N")
s = S.count("S")
w = S.count("W")
e = S.count("E")

if (n > 0) ^ (s > 0):
    res = False

if (w > 0) ^ (e > 0):
    res = False

if res:
    print("Yes")
else:
    print("No")

