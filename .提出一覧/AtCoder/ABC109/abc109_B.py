N = int(input())
W = [input() for _ in range(N)]

res = True

dic = {}

last = ""

for w in W:
    if last != "":
        if w in dic:
            res = False
        if not w[0] == last:
            res = False

    dic[w] = 1
    last = w[-1]


if res:
    print("Yes")
else:
    print("No")