H, W = map(int, input().split())
A = [input() for _ in range(H)]

t = ""
for i in range(W + 2):
    t += "#"
t += "\n"

res = ""

res += t

for a in A:
    res += "#{0}#\n".format(a)

res += t

print(res, end="")