N = int(input())
s = input()
t = input()

n = 0

for i in range(min(len(s), len(t)) + 1):
    if s[-i:] == t[:i]:
        n = i

print(len(s) + len(t) - n)

