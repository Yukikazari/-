w = input()

s = "abcdefghijklmnopqrstuvwxyz"

dic = {}

for o in s:
    dic[o] = 0

for o in w:
    dic[o] += 1

for num in dic.values():
    if num % 2 == 1:
        print("No")
        exit()

print("Yes")