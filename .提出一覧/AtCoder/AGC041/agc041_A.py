import math

N, A, B= map(int, input().split())

if (A - B) % 2 == 0:
    print(abs(A - B) // 2)

else:

    t1 = A - 1
    t2 = B - 1
    t3 = N - A
    t4 = N - B

    t = min(t1, t2, t3, t4)

    res = t + 1 + (abs(A - B) - 1) // 2
    
    print(res)