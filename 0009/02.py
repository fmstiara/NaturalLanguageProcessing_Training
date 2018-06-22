# 文字列を交互に連結
p = "パトカー"
t = "タクシー"

# 'x'.join([])で[]をxで連結する
# zip
print(''.join([char1 + char2 for char1, char2 in zip(p, t)]))
