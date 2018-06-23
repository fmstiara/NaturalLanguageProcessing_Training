# unixコマンドの場合
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt
# cutはタブ区切りでフィールドを選択して出力できる。

# 文章の1列目と2列目をそれぞれ取り出す。
# 行じゃなくて列!!

with open("hightemp.txt") as f1, open("col1.txt","w") as f2, open("col2.txt","w") as f3:
    cols=list( zip(*[row.split("\t") for row in f1]) )
    f2.write("\n".join(cols[0]))
    f3.write("\n".join(cols[1]))