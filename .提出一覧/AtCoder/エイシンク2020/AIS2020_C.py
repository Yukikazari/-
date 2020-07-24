N = int(input())

res = [0] * N


for x in range(1, 102):
    for y in range(1, 102):
        for z in range(1, 102):
            t1 = (x + y + z) ** 2

            if t1 > 15000:
                break

            n = t1 - x * y - y * z - z * x - 1
            
            if n >= N or n < 0:
                break
            res[n] += 1

for o in res:
    print(o)