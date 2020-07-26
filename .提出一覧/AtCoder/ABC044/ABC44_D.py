import math

n = int(input())
s = int(input())


r = 0

if n == s:
    print(n + 1)
    exit()
elif n < s:
    print(-1)
    exit()

sq = int(math.sqrt(n))


# 2 <= d <= √n
for i in range(2, sq+1):
    nt = n
    st = 0

    while nt > 0:
        st += nt % i
        nt //= i

    if st == s:
        print(i)
        exit()
    
# √n < d <= n
for i in range(sq, 0, -1):
    b = (n - s) // i + 1
    
    st = n % b + n // b

    if n // b != b and st == s:
        print(b)
        exit()

print(-1)