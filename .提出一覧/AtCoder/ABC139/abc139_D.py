N = int(input())

if N == 1:
    print(0)

else:
    res = N * (N + 1) // 2 - N
    print(res)