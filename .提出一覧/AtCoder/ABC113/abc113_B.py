N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

t = 10 ** 9
r = 0

for i in range(N):
    x = T - H[i] * 6 / 1000
    tt = abs(A - x)
    if t > tt:
        t = tt
        r = i + 1
        
print(r)