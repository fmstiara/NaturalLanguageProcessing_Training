# 暗号文

# chr(文字コード) -> 文字
# ord(文字) -> 文字コード
def cipher(string: str):
    return ''.join( chr(219 - ord(c)) if 'a'<=c<='z' else c for c in string)

if __name__=="__main__":
    sentence="こんにちは世界、Hello world!!"
    ciphertext = cipher(sentence)
    print(sentence)
    print(ciphertext)
    print(cipher(ciphertext))