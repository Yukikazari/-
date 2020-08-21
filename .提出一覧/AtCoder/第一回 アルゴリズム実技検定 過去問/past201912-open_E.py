
#= input()
N, Q = map(int, input().split())

users = [[False]*N for _ in range(N)]

for _ in range(Q):
    s = list(input().split())
    a = int(s[1]) - 1
    if len(s) == 3:
        b = int(s[2]) - 1
    if s[0] == "1":
        users[a][b] = True

    elif s[0] == "2":
        for i in range(N):
            if users[i][a]:
                users[a][i] = True

    else:
        t = []
        for i in range(N):
            if users[a][i]:
                t.append(i)

        for i in t:
            for j in range(N):
                if users[i][j]:
                    users[a][j] = True

for i in range(N):
    ans = ""
    for j in range(N):
        if i != j:
            if users[i][j]:
                ans += "Y"
            else:
                ans += "N"

        else:
            ans += "N"

    print(ans)