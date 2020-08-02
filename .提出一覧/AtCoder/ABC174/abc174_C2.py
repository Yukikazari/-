#  mod Nの取りうる値の上限はN-1なのでN-1回のループで解が出なければ-1でいい
#  modの値が同じになった場合ループになるためexitする

K = int(input())

mod = 7 % K

res = {}

i = 1

while not mod in res:
    if mod == 0:
        print(i)
        exit()

    res[mod] = 1
    mod = (mod * 10 + 7) % K
    i += 1

print(-1)