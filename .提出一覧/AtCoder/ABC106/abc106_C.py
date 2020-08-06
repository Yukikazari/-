S = input()
K = int(input())

for i, s in enumerate(S, 1):
    if i == K:
        print(s)
        exit()

    if s != "1":
        print(s)
        exit()
