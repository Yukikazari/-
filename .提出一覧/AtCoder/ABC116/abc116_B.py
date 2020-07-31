s = int(input())

a = [s]
last = s

while True:
    if last % 2 == 0:
        last //= 2
    else:
        last = last * 3 + 1

        
    if last in a:
        print(len(a) + 1)
        exit()
    else:
        a.append(last)