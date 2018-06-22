from random import shuffle

sentence="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
def typo(word):
    middle=list(word[1:-1])
    shuffle(middle)
    return word[0]+''.join(middle)+word[-1]
print(' '.join(typo(w) if len(w)>4 else w for w in sentence.split()))