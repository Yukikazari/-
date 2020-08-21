N= int(input())
A= [int(input()) for _ in range(N)]

for i in range(1, N):
    ai = A[i] - A[i - 1]
    if ai > 0:
        print("up", ai)
    elif ai == 0:
        print("stay")
    else:
        print("down", -ai)

