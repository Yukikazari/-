N = int(input())
S = {}
for _ in range(N):
    s = input()
    if s in S:
        S[s] += 1
    else:
        S[s] = 1

M = int(input())
T = {}
for _ in range(M):
    t = input()
    if t in T:
        T[t] += 1
    else:
        T[t] = 1

res = 0

for s in S:
    if s in T:
        if S[s] - T[s] > 0:
            res = max(res, S[s] - T[s])

    else:
        res = max(res, S[s])

print(res)

