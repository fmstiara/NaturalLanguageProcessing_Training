# unixコマンドの場合
# sed 's/\t/ /g' hightemp.txt
# ↑のsはsedコマンドを正規表現で比べるという意味

# 文章内のタブをスペースに変換する

with open('hightemp.txt', 'r') as f:
    print ( (f.read()).replace('\t',',') )


