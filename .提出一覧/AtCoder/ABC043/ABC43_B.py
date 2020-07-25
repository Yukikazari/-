s = input()

res = ""

for do in s:
    if do == "B":
        if len(res) != 0:
            res = res[0:len(res)-1]
        
    else:
        res += do

print(res)