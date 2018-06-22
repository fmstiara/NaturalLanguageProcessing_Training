# 円周率
s3 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# str.strip("x")でstringからxという文字をすべて抜き取る
# str.split("x")でstringをxで分ける
# どちらも指定しなければ、空白文字で実行
count = [ len(word.strip(".,")) for word in s3.split() ]

print(count)
