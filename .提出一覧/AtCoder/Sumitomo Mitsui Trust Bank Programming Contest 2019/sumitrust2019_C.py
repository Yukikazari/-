X = int(input())

x1 = X // 100
x2 = X % 100

if x2 <= x1 * 5:
    print(1)
else:
    print(0)