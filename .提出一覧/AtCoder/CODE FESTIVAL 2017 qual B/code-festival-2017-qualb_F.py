N= int(input())
D= list(map(int, input().split()))
M= int(input())
T= list(map(int, input().split()))

Ddic = {}
for d in D:
    if d in Ddic:
        Ddic[d] += 1
    else:
        Ddic[d] = 1

Tdic = {}
for t in T:
    if t in Tdic:
        Tdic[t] += 1
    else:
        Tdic[t] = 1

ans = True

for t in Tdic:
    if not t in Ddic:
        ans = False
    elif Tdic[t] > Ddic[t]:
        ans = False

if ans:
    print("YES")

else:
    print("NO")