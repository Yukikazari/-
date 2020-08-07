A = list(map(int, input()))

dic = {1: "+", 0: "-"}

for i in range(2 ** 3):
    t = A[0]
    s = str(A[0])
    for j in range(3):
        if (i >> j) & 1:
            t += A[j + 1]
            s += dic[1] + str(A[j + 1])
        else:
            t -= A[j + 1]
            s += dic[0] + str(A[j + 1])
            
    if t == 7:
        print(s + "=7")
        exit()
