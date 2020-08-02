import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

#  めぐる式二分探索で実装

def calc(x):
    count = 0
    for a in A:
        count += (a - 1) // x

    return count <= K

ok = 10 ** 9
ng = 0

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    
    if calc(mid):
        ok = mid
    else:
        ng = mid

print(ok)
