N = int(input())
S = [input() for _ in range(N)]

S.sort()

maxint = 1

sdic = {}

for s in S:
    if s in sdic:
        sdic[s] += 1
        if sdic[s] > maxint:
            maxint = sdic[s]

    else:
        sdic[s] = 1

for s in sdic:
    if sdic[s] == maxint:
        print(s)