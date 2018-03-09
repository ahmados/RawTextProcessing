import nltk
import sys
from nltk import word_tokenize
import numpy as np

def intersection(a, b):
    return list(set(a) & set(b))

def digits_and_letters(tokens):
    our_tokens = list()
    for a in tokens:
        if (((ord(a[0]) - ord('a')) >= 0) and ((ord(a[0]) - ord('a')) <= 25)):
            our_tokens.append(a)
        if (((ord(a[0]) - ord('0')) >= 0) and ((ord(a[0]) - ord('0')) <= 9)):
            our_tokens.append(a)
        if (((ord(a[0]) - ord('A')) >= 0) and ((ord(a[0]) - ord('A')) <= 25)):
            our_tokens.append(a)
    return our_tokens

def how_much_similar(tokens_1, tokens_2):
    our_tokens_1 = digits_and_letters(tokens_1)
    our_tokens_2 = digits_and_letters(tokens_2)
    intersec = intersection(our_tokens_1, our_tokens_2)
    return len(intersec)

if __name__ == "__main__":
    args = sys.argv
    if (len(args) < 3):
        print('PLEASE ENTER MORE THAN TWO FILES, LIKE BELOW:')
        print('python words.py 1.txt 2.txt')
        sys.exit()
    # f_1 = open(args[1])
    # raw_1 = f_1.read()
    # tokens_1 = word_tokenize(raw_1)
    # f_2 = open(args[2])
    # raw_2 = f_2.read()
    # tokens_2 = word_tokenize(raw_2)

    # our_tokens_1 = digits_and_letters(tokens_1)
    # our_tokens_2 = digits_and_letters(tokens_2)
    # intersec = intersection(our_tokens_1, our_tokens_2)
    # print(intersec)
    # print("THIS TEXTS HAVE ", \
    #     (len(intersec)), " WORDS IN COMMON")
    texts = list()
    counter = 0
    for i in range(1, len(args)):
        path = args[i]
        f = open(path)
        raw = f.read()
        texts.append(word_tokenize(raw))
        counter += 1
    similarity = np.zeros((counter, counter), dtype=int)
    for i in range(counter):
        for j in range(counter):
            if (i != j):
                similarity[i][j] = how_much_similar(texts[i], texts[j])
    print(similarity)
