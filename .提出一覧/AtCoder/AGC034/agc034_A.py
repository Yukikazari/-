N, A, B, C, D = map(int, input().split())
S= input()

A -= 1
B -= 1
C -= 1
D -= 1

ok = []
ng = []

for i in range(1, N - 1):
    if S[i] == S[i + 1] and S[i] == "#":
        ng.append(i)
    elif S[i - 1] == S[i] and S[i] == S[i + 1] and S[i] == ".":
        ok.append(i)

for ngi in ng:
    if (A < ngi and ngi < C) or (B < ngi and ngi < D):
        print("No")
        exit()

if C < D:
    print("Yes")

else:
    for oki in ok:
        if B <= oki and oki <= D:
            print("Yes")
            exit()

    print("No")
