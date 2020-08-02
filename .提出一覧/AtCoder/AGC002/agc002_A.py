a, b = map(int, input().split())

if a < 0 and 0 < b:
    print("Zero")
elif 0 < a:
    print("Positive")
else:
    ab = abs(a - b)
    if ab % 2 == 1:
        print("Positive")
    else:
        print("Negative")