# 準備運動編

# 文字列反転
# str[start:end:step]

s1 = "template text"
print(s1[::-1])


# 奇数文字目を取り出し
s2 = "パタトクカシーーー"
print(s2[::2])

# 偶数文字ならスタートをずらす
print(s2[1::2])


# 文字列を交互に連結
p = "パトカー"
t = "タクシー"

# 'x'.join([])で[]をxで連結する
print(''.join([char1 + char2 for char1, char2 in zip(p, t)]))

# 円周率
s3 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
