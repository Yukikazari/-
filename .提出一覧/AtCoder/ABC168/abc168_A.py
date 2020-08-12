N = int(input())

hon = [2, 4, 5, 7, 9]
pon = [0, 1, 6, 8]

n = N % 10

if n in hon:
    print("hon")
elif n in pon:
    print("pon")
else:
    print("bon")

