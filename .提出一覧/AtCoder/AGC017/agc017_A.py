N,P= map(int, input().split())
A= list(map(int, input().split()))
A = [A[i] % 2 for i in range(N)] 
even = A.count(0)
odd = A.count(1)

anseven = 1
ansodd = 1

dic = {0:1}
for i in range(1, 51):
    dic[i] = dic[i - 1] * i

#  偶数i個選ぶ
for i in range(1, even + 1):
    anseven += dic[even] // dic[even - i] // dic[i]

if P == 0:
    #  奇数i個選ぶ
    for i in range(2, odd + 1, 2):
        ansodd += dic[odd] // dic[odd - i] // dic[i]

else:
    if odd == 0:
        print(0)
        exit()
    ansodd = 0
    #  奇数i個選ぶ
    for i in range(1, odd + 1, 2):
        ansodd += dic[odd] // dic[odd - i] // dic[i]

print(anseven * ansodd)