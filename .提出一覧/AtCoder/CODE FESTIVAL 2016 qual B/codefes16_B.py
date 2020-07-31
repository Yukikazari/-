N, A, B = map(int, input().split())
s = list(map(str, input()))

clear = 0

ab = A + B
b = 0

for obj in s:
    if clear < ab:
        if obj == "a":
            print("Yes")
            clear += 1
        elif obj == "b" and b < B:
            print("Yes")
            clear += 1
            b += 1
        else:
            print("No")

    else:
        print("No")