N = int(input())
A = list(map(int, input().split()))

dic = {i: 0 for i in range(10 ** 5 + 1)}

for a in A:
    dic[a] += 1

ans = 0

for i in range(1, 10 ** 5):
    ans = max(ans, dic[i - 1] + dic[i] + dic[i + 1])
    
print(ans)