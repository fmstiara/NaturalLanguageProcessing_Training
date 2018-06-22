# n-gram
s5 = "I am an NLPer"
charGram = [ s5[i:i+2] for i in range(len(s5)-1) ]

words = [ word.strip(".,") for word in s5.split() ]
wordGram = [ "-".join(words[i:i+2]) for i in range(len(words)-1) ]

print(charGram, wordGram)