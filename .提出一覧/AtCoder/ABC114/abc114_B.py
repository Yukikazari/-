S = input()

res = 753

for i in range(len(S) - 2):
    s = int(S[i: i + 3])
    res = min(res, abs(s - 753))
    
print(res)