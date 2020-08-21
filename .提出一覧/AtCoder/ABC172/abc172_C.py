def is_ok(arg):
    return not Alist[arg] <= t
    

def bisect(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Alist = [0]
for i in range(N):
    Alist.append(Alist[i] + A[i])

ans = 0
for i in range(N+1):
    if Alist[i] <= K:
        ans = i
    else:
        break

b = 0
for i in range(M):
    b += B[i]
    t = K - b

    if t >= 0:
        res = bisect(N + 1, -1)
        ans = max(ans, i + res)

    else:
        break

print(ans)