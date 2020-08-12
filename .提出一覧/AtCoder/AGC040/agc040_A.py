S = list(input())

#  ><は0でいいのか
#  同様に S[0]==<とS[-1]==>も0でいい
#  制約的にNlogNくらいまでは十分許容範囲だし><は0で埋めてindex保持、そこから単調増加で組むのが良さそう？

#  3回ループさせる形で実装してみる

tmp = [-1] * (len(S) + 1)

for i in range(len(S) - 1):
    if S[i] == ">" and S[i + 1] == "<":
        tmp[i + 1] = 0
        
if S[0] == "<":
    tmp[0] = 0

if S[-1] == ">":
    tmp[-1] = 0

for i in range(len(S)):
    if S[i] == "<":
        tmp[i + 1] = tmp[i] + 1
        
for i in range(len(S) - 1, -1, -1):
    if S[i] == ">":
        tmp[i] = max(tmp[i], tmp[i + 1] + 1)

print(sum(tmp))
        
