A = [list(map(int, input().split())) for _ in range(3)]

N = int(input())
B = [int(input()) for _ in range(N)]

a = []

Atf = [[False] * 3 for _ in range(3)]

for i in range(3):
    for aa in A[i]:
        a.append(aa)

for b in B:
    if b in a:
        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    Atf[i][j] = True

res = False

for i in range(3):
    if Atf[i][0] and Atf[i][1] and Atf[i][2]:
        res = True
        break
    elif Atf[0][i] and Atf[1][i] and Atf[2][i]:
        res = True
        break

if not res:
    if Atf[0][0] and Atf[1][1] and Atf[2][2]:
        res = True
    elif Atf[0][2] and Atf[1][1] and Atf[2][0]:
        res = True
 

if res:
    print("Yes")
else:
    print("No")
        
