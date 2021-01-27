#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

t1 = set()
t2 = set()

li = []

t1.add(AB[0][0])
t2.add(AB[0][1])

for i in range(1, N):
    a, b = AB[i]
    
    if a in t1 and a in t2:
        t1.add(b)
        t2.add(b)
    elif b in t1 and b in t2:
        t1.add(a)
        t2.add(a)
    elif a in t1 or b in t2:
        t2.add(a)
        t1.add(b)
    elif b in t1 or a in t2:
        t1.add(a)
        t2.add(b)

    else:
        li.append(i)

ans = 0

while li:
    n1 = len(t1)
    n2 = len(t2)
    tli = []
    for i in li:
        a, b = AB[i]
    
        if a in t1 and a in t2:
            t1.add(b)
            t2.add(b)
        elif b in t1 and b in t2:
            t1.add(a)
            t2.add(a)
        elif a in t1 or b in t2:
            t2.add(a)
            t1.add(b)
        elif b in t1 or a in t2:
            t1.add(a)
            t2.add(b)

        else:
            tli.append(i)

    if len(li) == len(tli):
        ans = max(len(t1), len(t2))
        t1 = set()
        t2 = set()

        num = tli.pop()
        t1.add(AB[num][0])
        t2.add(AB[num][1])    

    li = tli


print(ans + max(len(t1), len(t2)))
# print(t1, t2)