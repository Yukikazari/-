S = input()

ls = len(S)
ans = (ls - 1) * 2

for i in range(1, ls - 1):
    up = ls - i - 1
    down = ls - up - 1
    if S[i] == "U":
        ans += up + down * 2

    else:
        ans += up * 2 + down

print(ans)
