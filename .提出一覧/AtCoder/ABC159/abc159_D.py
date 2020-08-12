import math

N = int(input())
A = list(map(int, input().split()))

dic = {}
for a in A:
    if not a in dic:
        dic[a] = 1
    else:
        dic[a] += 1

ans = 0
for a in dic:
    if dic[a] > 1:
         ans += dic[a] * (dic[a] - 1) // 2

ansdic = {}

for a in dic:
    ansdic[a] = ans
    if dic[a] > 1:
        ansdic[a] = ans - (dic[a] - 1)

for a in A:
    print(ansdic[a])
