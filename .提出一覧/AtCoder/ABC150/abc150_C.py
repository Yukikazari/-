N = int(input())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))

#  iの階乗
x = [1] * (N + 1)

for i in range(1, N + 1):
    x[i] = x[i - 1] * i
    

res1 = 1
res2 = 1

s1 = [i for i in range(1, N + 1)]
s2 = [i for i in range(1, N + 1)]

for p in P:
    for i in range(len(s1)):
        if p == s1[i]:
            s1.pop(i)
            t = i - 1
            break

    res1 += t * x[len(s1)]

for q in Q:
    for i in range(len(s2)):
        if q == s2[i]:
            s2.pop(i)
            t = i - 1
            break

    res2 += t * x[len(s2)]

print(abs(res1 - res2))