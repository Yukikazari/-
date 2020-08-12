R, G, B, N = map(int, input().split())

ans = 0

for r in range(N // R + 1):
    for g in range(N // G + 1):
        if (N - r * R - g * G) % B == 0 and r * R + g * G <= N:
            ans += 1

print(ans)

