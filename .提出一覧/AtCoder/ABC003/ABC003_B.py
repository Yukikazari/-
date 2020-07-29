S, T= [input(), input()]

atto = ["a", "t", "c", "o", "d", "e", "r"]

win = "You can win"
lose = "You will lose"

res = True

for i in range(len(S)):
    if S[i] != T[i]:
        if (S[i] in atto and T[i] == "@") or (S[i] == "@" and T[i] in atto):
            pass
        else:
            res = False
            break


if res:
    print(win)
else:
    print(lose)