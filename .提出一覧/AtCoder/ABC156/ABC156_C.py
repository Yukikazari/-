import math

N = int(input())
X = list(map(int, input().split()))

#  O(100N)とかになりそうだし全探索で良さげ

xmin = 10 ** 7

for i in range(1, 101):
    xsum = 0
    for j in range(N):
        xsum += (X[j] - i) ** 2
    xmin = min(xmin, xsum)

print(xmin)