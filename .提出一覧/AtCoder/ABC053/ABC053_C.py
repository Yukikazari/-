x = int(input())

s = x // 11
t = x % 11
if t > 6:
    print(s * 2 + 2)
elif t > 0:
    print(s * 2 + 1)
else:
    print(s * 2)