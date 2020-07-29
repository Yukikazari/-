S = input()
#  +のかず 0 - len(S) - 1

r = 0

s = len(S) - 1

for i in range(2 ** s):
    bit = []
    for j in range(s):
        if (i >> j) & 1:
            bit.append(j+1)

    for o in range(len(bit)):
        if o == 0:
            r += int(S[0: bit[o]])
        else:
            r += int(S[bit[o - 1] : bit[o]])
            
    if len(bit) == 0:
        r += int(S)
    else:
        r += int(S[bit[-1] :])
        
print(r)