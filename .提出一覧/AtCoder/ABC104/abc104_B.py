S = list(input())

if S[0] != "A":
    print("WA")
    exit()

S.pop(0)

res = True
c = False

for i in range(len(S)):
    if i == 0 or i == len(S) - 1:
        if not S[i].islower():
            res = False
    
    else:
        if S[i] == "C":
            if not c:
                c = True
            else:
                res = False

        else:
            if not S[i].islower():
                res = False

if res and c:
    print("AC")
else:
    print("WA")