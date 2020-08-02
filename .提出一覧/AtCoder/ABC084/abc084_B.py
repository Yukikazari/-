import re

A, B = map(int, input().split())
S = input()

m = re.match("([0-9]+)-([0-9]+)", S)

if m:
    t1 = m[1]
    t2 = m[2]
    if len(t1) == A and t1.isdecimal() and len(t2) == B and t2.isdecimal():
        print("Yes")
        exit()

print("No")