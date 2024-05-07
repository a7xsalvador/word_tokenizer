'''
Functions used for the tokenization of corpus, to know the frequency of a token.
'''
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

def word_frequency(token):
    dic={}
    for word in token:
        if word not in dic:
            dic[word]=1
        else:
            dic[word] += 1
    return dic

def sort_dic(dic):
    dic_sorted = {}
    dic_values = list(sorted(dic.values()))
    index = 0
    while len(dic) != len(dic_sorted):
        for i in dic.keys():
            if dic[i] == dic_values[index]:
                dic_sorted[i]=dic[i]
                index += 1
    return dic_sorted



def start():
    corpus = str(input("please enter a text "))
    print(tokenize(corpus))

if __name__ == '__main__':
    start()
