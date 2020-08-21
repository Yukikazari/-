import math
A, B, C, D = map(int, input().split())
CD = C * D // math.gcd(C, D)
ab = B - A + 1
c = B // C - (A - 1) // C
d = B // D - (A - 1) // D
cd = B // (CD) - (A - 1) // (CD)

print(ab - (c + d - cd))