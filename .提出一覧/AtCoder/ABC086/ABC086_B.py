import math

a, b = map(str, input().split())

ab = int(a + b)

if math.sqrt(ab).is_integer():
    print("Yes")
else:
    print("No")