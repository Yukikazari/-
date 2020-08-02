N, A, B = map(int, input().split())

ab = A + B

r1 = N // ab * A
r2 = min(A, N % ab)

print(r1 + r2)
