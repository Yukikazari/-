N = int(input())
a = list(map(int, input().split()))

minint = 10**9

if N == 2:
    print(abs(a[0] - a[1]))

else:
    s1 = s1 = sum(a[0:1])
    s2 = sum(a[1: N])
    for i in range(1, N - 1):
        s1 += a[i]
        s2 -= a[i]
        
        minint = min(minint, abs(s1 - s2))

    print(minint)