S = input()
T = input()

for _ in range(len(S) + 1):
    if S == T:
        print("Yes")
        exit()

    s1 = S[0]
    s2 = S[1:]
    S = s2 + s1

print("No")