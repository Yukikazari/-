N = input()

ans = 0
for n in N:
    ans += int(n)

if ans % 9 == 0:
    print("Yes")

else:
    print("No")