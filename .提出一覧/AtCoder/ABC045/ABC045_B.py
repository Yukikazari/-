sa = list(map(str, input()))
sb = list(map(str, input()))
sc = list(map(str, input()))

turn = 0

while True:
    s = ""
    if turn == 0:
        if len(sa) != 0:
            s = sa.pop(0)
        else:
            print("A")
            exit()
    elif turn == 1:
        if len(sb) != 0:
            s = sb.pop(0)
        else:
            print("B")
            exit()
    else:
        if len(sc) != 0:
            s = sc.pop(0)
        else:
            print("C")
            exit()

    if s == "a":
        turn = 0
    elif s == "b":
        turn = 1
    else:
        turn = 2