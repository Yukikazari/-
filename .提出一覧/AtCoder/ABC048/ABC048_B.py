a, b, x = map(int, input().split())

r = b // x - a // x
if a % x == 0:
    r += 1

print(r)