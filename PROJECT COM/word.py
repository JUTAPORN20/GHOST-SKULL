import random
def vocabulary_list():
    flie = open('out_word.txt','r')
    flie = flie.readlines()
    word = []
    for w in flie:
        w = w.strip("\n")
        word += [w]
        

    flie = open('vocabulary.txt','r')
    flie = flie.readlines()
    for w in flie:
        w = w.strip("\n")
        if w not in word:
            word += [w]
    random.shuffle(word)
    return word
            
