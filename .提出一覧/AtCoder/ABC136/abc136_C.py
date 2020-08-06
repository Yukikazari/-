N = int(input())
H = list(map(int, input().split()))

res = True

for i in range(N - 1):
    if H[i + 1] > H[i]:
        H[i + 1] -= 1
        
    if H[i + 1] < H[i]:
        res = False
        break

if res:
    print("Yes")
else:
    print("No")