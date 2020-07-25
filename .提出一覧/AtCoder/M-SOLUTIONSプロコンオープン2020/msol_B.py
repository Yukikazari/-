A, B, C = map(int, input().split())

K = int(input())

c = 0

while True:
    if A >= B:
        B *= 2
        c += 1
    elif B >= C:
        C *= 2
        c += 1
    else:
        break

if c <= K:
    print("Yes")

else:
    print("No")