A, B, C = map(int, input().split())

ab = A % B

for i in range(B + 1):
    if ab * i % B == C:
        print("YES")
        exit()

print("NO")