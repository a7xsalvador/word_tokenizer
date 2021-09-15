
def tokenize(corpus):
    word = ''
    counter = 0 
    tokenized = []
    len_corpus = len(corpus)
    for i in corpus:
        if i == ' ' or counter +1 == len_corpus:
            tokenized.append(word)
            word = ''
        else:
            word += i
        counter += 1

    return tokenized


def start():
    corpus = str(input("please enter a text "))
    print(tokenize(corpus))

if __name__ == '__main__':
    start()
