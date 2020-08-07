N = int(input())

def mod(num):
    return num % (10 ** 9 + 7)
    
ans = 1

for i in range(2, N + 1):
    ans = mod(ans * i)

print(ans)