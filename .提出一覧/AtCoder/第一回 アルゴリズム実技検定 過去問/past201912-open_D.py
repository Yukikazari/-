N = int(input())

dic = {i: False for i in range(1, N + 1)}

after = -1

for _ in range(N):
    a = int(input())
    if dic[a]:
        after = a

    dic[a] = True

if after == -1:
    print("Correct")

else:
    for key in dic:
        if not dic[key]:
            print(after, key)
