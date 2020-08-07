A, B, C, D = map(int, input())

if A + B + C + D == 7:
    print("{0}+{1}+{2}+{3}=7".format(A, B, C, D))

elif A + B + C - D == 7:
    print("{0}+{1}+{2}-{3}=7".format(A, B, C, D))

elif A + B - C + D == 7:
    print("{0}+{1}-{2}+{3}=7".format(A, B, C, D))

elif A + B - C - D == 7:
    print("{0}+{1}-{2}-{3}=7".format(A, B, C, D))

elif A - B + C + D == 7:
    print("{0}-{1}+{2}+{3}=7".format(A, B, C, D))

elif A - B + C - D == 7:
    print("{0}-{1}+{2}-{3}=7".format(A, B, C, D))

elif A - B - C + D == 7:
    print("{0}-{1}-{2}+{3}=7".format(A, B, C, D))

else:
    print("{0}-{1}-{2}-{3}=7".format(A, B, C, D))