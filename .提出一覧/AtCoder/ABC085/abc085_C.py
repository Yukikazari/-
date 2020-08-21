N, Y= map(int, input().split())

Y //= 1000

for x in range(N + 1):
    for y in range(N-x+1):
        z = N - (x + y)
        yen = x * 10 + y * 5 + z
        if Y == yen:
            print(x, y, z)
            exit()

print(-1, -1, -1)