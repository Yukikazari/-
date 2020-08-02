#import
#import math
#import numpy as np
K = int(input())

if K == 7:
    print(1)
    exit()

t = 7 % K
    
for i in range(1, K * 2):
    if t == 0:
        print(i)
        exit()

    t = (t * 10 + 7) % K

print(-1)