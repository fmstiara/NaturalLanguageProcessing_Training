# 集合
word1="paraparaparadise"
word2="paragraph"

# setは集合を表すデータ型。リストとは異なる
X=set( [word1[i:i+2] for i in range(len(word1)-1)] )
Y=set( [word2[i:i+2] for i in range(len(word2)-1)] )

print("X="+str(X))
print("Y="+str(Y))
print ("和集合:"+str(X|Y))
print ("差集合:"+str(X-Y))
print ("積集合:"+str(X&Y))
if 'se' in X:
    print( "'se'はXに含まれる" )
if 'se' in Y:
    print( "'se'はYに含まれる" )