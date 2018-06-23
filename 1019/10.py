# Unixコマンドの場合
# wc -l <ファイル名> 行数を表示
# wc -c <ファイル名> バイト数を表示
# wc -m <ファイル名> 文字数を表示
# wc -L <ファイル名> 最長行を表示（GNU 拡張）
# wc -w <ファイル名> 単語数を表示

# 行数を表示

with open('hightemp.txt', 'r') as f:
    print( len( f.readlines() ) )