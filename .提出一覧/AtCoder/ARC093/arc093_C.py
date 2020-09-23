N = int(input())
A = list(map(int, input().split()))

money = 0

last = 0
for a in A:
    money += abs(last - a)
    last = a
money += abs(last)

for i in range(N):
    if i == 0:
        t1 = A[i]
        t2 = A[i + 1]
        if int(t1 >= 0) ^ int(t2 >= 0):
            print(money - abs(t1) * 2)
        elif abs(t1) > abs(t2):
            print(money - abs(t1 - t2) * 2)
        else:
            print(money)

    elif i == N - 1:
        t1 = A[i]
        t2 = A[i - 1]
        if int(t1 >= 0) ^ int(t2 >= 0):
            print(money - abs(t1) * 2)
        elif abs(t1) > abs(t2):
            print(money - abs(t1 - t2) * 2)
        else:
            print(money)

    else:
        a0 = A[i - 1]
        a1 = A[i]
        a2 = A[i + 1]
        if (a0 <= a1 and a1 <= a2) or (a0 >= a1 and a1 >= a2):
            print(money)
        elif (a0 <= a2 and a2 <= a1) or (a0 >= a2 and a2 >= a1):
            print(money - abs(a2 - a1) * 2)
        else:
            print(money - abs(a1 - a0) * 2)