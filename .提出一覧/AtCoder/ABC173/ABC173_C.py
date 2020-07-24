import copy
H, W, K = map(int, input().split())

count = 0

res = 0

c = []
for j in range(H):
    s = list(map(str, input()))
    c.append(s)
    count += s.count("#")

m = 0
for i in range(2 ** H):
    t = copy.deepcopy(c)
    count_tmp = copy.deepcopy(count)
    for j in range(H):
        if((i>>j) & 1):
            for a in range(W):
                if t[j][a] == "#":
                    t[j][a] = "@"
                    count_tmp -= 1
    for k in range(2 ** W):
        count_tmp2 = copy.deepcopy(count_tmp)
        t2 = copy.deepcopy(t)
        for l in range(W):
            if((k>>l) & 1):
                for b in range(H):
                    if t2[b][l] == "#":
                        t2[b][l] = "@"
                        count_tmp2 -= 1
        m += 1
        if count_tmp2 == K:
            res += 1

print(res)
