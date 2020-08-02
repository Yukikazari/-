S = input()

abc = "abcdefghijklmnopqrstuvwxyz"

dic = {s: True for s in abc}

for s in S:
    if dic[s]:
        dic[s] = False

for d in dic:
    if dic[d]:
        print(d)
        exit()

print("None")