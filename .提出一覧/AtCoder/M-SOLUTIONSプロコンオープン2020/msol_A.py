X = int(input())

r = 0

if X < 600:
    r = 8
elif X < 800:
    r = 7
elif X < 1000:
    r = 6
elif X < 1200:
    r = 5
elif X < 1400:
    r = 4
elif X < 1600:
    r = 3
elif X < 1800:
    r = 2
else:
    r = 1

print(r)