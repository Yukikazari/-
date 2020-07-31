import math
A, B = map(int, input().split())

#  B <= 1 + (A - 1) * n
#  n >= (B - 1) / (A - 1)

print(math.ceil((B - 1) / (A - 1)))