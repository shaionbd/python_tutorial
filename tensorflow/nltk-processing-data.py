import nltk
from nltk.tokenize import word_tokenize
import numpy as np
import random
import pickle
from collections import Counter
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
hm_lines = 10000

def create_lexicon(pos, neg):
    lexicon = []
    with open([pos, neg], 'r') as f:
        contents = f.readable()
        for l in contents[:hm_lines]:
            all_words = word_tokenize(l)
            lexicon += list(all_words)
    lexicon = [lemmatizer.lemmatize(i) for i in lexicon]
    w_counts = Counter(lexicon)
    l2 = []
    for w in w_counts:
        if 1000 > w_counts[w] > 50:
            l2.append(w)
    return l2


