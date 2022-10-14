import nltk
import numpy as np
nltk.download('stopwords')
nltk.download('punkt')

def clean(s):
    r = []
    stopwords = nltk.corpus.stopwords.words('english')
    for items in s:
        words = nltk.tokenize.word_tokenize(items)
        words_new = [i for i in words if i not in stopwords]
        r.append(words_new)
    return r