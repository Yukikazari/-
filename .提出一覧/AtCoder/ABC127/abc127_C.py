N, M = map(int, input().split())

st = 0
en = N

for _ in range(M):
    l, r = map(int, input().split())
    st = max(st, l)
    en = min(en, r)

print(max(en - st + 1, 0))