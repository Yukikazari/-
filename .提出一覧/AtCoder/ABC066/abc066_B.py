S = input()

S = S[:-1]

if len(S) % 2 == 1:
    S = S[:-1]

while True:
    half = len(S) // 2 
    if S[:half] == S[half:]:
        print(len(S))
        exit()

    S = S[:-2]