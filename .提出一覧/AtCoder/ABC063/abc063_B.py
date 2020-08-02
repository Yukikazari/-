S = input()

sdic = {}

for s in S:
    if s in sdic:
        print("no")
        exit()

    sdic[s] = 1

print("yes")