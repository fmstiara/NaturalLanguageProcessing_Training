# テンプレートによる文生成
def mkStr(x, y, z: str):
    return "{0}時の{1}は{2}".format(x, y, z)

if __name__=="__main__":
    print(mkStr(12, "気温", 22.4))