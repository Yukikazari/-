A, B, C = map(int, input().split())

if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    print(0)

else:
    if A >= B and A >= C:
        print(B * C)

    elif B >= C:
        print(A * C)

    else:
        print(A * B)