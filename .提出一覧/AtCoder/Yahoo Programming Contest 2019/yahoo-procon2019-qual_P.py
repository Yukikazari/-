K,A,B= map(int, input().split())

if A + 2 >= B:
    print(K + 1)

else:
    K -= A - 1
    q, m = divmod(K, 2)
    print((B - A) * q + A + m)