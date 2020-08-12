R, G, B, N = map(int, input().split())

ans = 0

for i in range(N + 1):
    for j in range(N + 1):
        rg = R * i + G * j

        if rg <= N:
            if (N - rg) % B == 0:
                ans += 1

        else:
            break

print(ans)

