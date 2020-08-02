import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

#  にぶたん！ 半開区間二分探索は正義

def calc(x):
    count = 0
    for a in A:
        count += (a - 1) // x

    return count <= K

A.sort(reverse=True)

r = 10 ** 9
l = 0

while abs(r - l) > 1:
    mid = (r + l) // 2
    
    if calc(mid):
        r = mid
    else:
        l = mid

print(r)
