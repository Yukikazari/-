s= list(input())

abc = "abcdefghijklmnopqrstuvwxyz"

ans = len(s)

for a in abc:
    if a in s:
        t = s.index(a)
        anst = t
        for i in range(t+1, len(s)):
            if s[i] == a:
                anst = max(anst, i - t - 1)
                t = i

        anst = max(anst, len(s) - t - 1)

        ans = min(ans, anst)

print(ans)