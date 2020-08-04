A, B = [int(input()), int(input())]

#  Pythonのintは無限長なので勝ち
#  cppとかだとllでも100桁は不可のはずなのでstr配列で受けてlengh比較→各桁の値比較でいけそう

if A > B:
    print("GREATER")
elif A == B:
    print("EQUAL")
else:
    print("LESS")