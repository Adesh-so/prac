
# Practical 7: Text Analytics using NLTK and TF-IDF

# ==========================================
# STEP 1: IMPORT LIBRARIES AND DOWNLOAD NLTK DATA
# ==========================================

import nltk
import pandas as pd
import numpy as np
import re
import math

# Download required NLTK datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')

# ==========================================
# STEP 2: TEXT TOKENIZATION
# ==========================================

text = "Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentences is called Tokenization."

# Sentence Tokenization
from nltk.tokenize import sent_tokenize

tokenized_text = sent_tokenize(text)

print("\nSentence Tokenization:")
print(tokenized_text)

# Word Tokenization
from nltk.tokenize import word_tokenize

tokenized_word = word_tokenize(text)

print("\nWord Tokenization:")
print(tokenized_word)

# ==========================================
# STEP 3: REMOVE PUNCTUATIONS AND STOPWORDS
# ==========================================

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

print("\nEnglish Stopwords:")
print(stop_words)

text = "How to remove stop words with NLTK library in Python?"

# Remove punctuation and special characters
text = re.sub('[^a-zA-Z]', ' ', text)

# Convert text to lowercase and tokenize
tokens = word_tokenize(text.lower())

filtered_text = []

for w in tokens:

    if w not in stop_words:
        filtered_text.append(w)

print("\nTokenized Sentence:")
print(tokens)

print("\nFiltered Sentence:")
print(filtered_text)

# ==========================================
# STEP 4: PERFORM STEMMING
# ==========================================

from nltk.stem import PorterStemmer

e_words = ["wait", "waiting", "waited", "waits"]

ps = PorterStemmer()

print("\nStemming Results:")

for w in e_words:

    rootWord = ps.stem(w)

    print(rootWord)

# ==========================================
# STEP 5: PERFORM LEMMATIZATION
# ==========================================

from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

text = "studies studying cries cry"

tokenization = nltk.word_tokenize(text)

print("\nLemmatization Results:")

for w in tokenization:

    print(
        "Lemma for {} is {}".format(
            w,
            wordnet_lemmatizer.lemmatize(w)
        )
    )

# ==========================================
# STEP 6: PERFORM POS TAGGING
# ==========================================

data = "The pink sweater fit her perfectly"

words = word_tokenize(data)

print("\nPOS Tagging Results:")

for word in words:

    print(nltk.pos_tag([word]))

# ==========================================
# STEP 7: TF-IDF IMPLEMENTATION
# ==========================================

documentA = 'Jupiter is the largest Planet'

documentB = 'Mars is the fourth planet from the Sun'

# ==========================================
# STEP 8: CREATE BAG OF WORDS
# ==========================================

bagOfWordsA = documentA.split(' ')

bagOfWordsB = documentB.split(' ')

print("\nBag of Words - Document A:")
print(bagOfWordsA)

print("\nBag of Words - Document B:")
print(bagOfWordsB)

# ==========================================
# STEP 9: CREATE UNIQUE WORDS
# ==========================================

uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))

print("\nUnique Words:")
print(uniqueWords)

# ==========================================
# STEP 10: COUNT WORD FREQUENCY
# ==========================================

numOfWordsA = dict.fromkeys(uniqueWords, 0)

for word in bagOfWordsA:

    numOfWordsA[word] += 1

numOfWordsB = dict.fromkeys(uniqueWords, 0)

for word in bagOfWordsB:

    numOfWordsB[word] += 1

print("\nWord Frequency - Document A:")
print(numOfWordsA)

print("\nWord Frequency - Document B:")
print(numOfWordsB)

# ==========================================
# STEP 11: COMPUTE TERM FREQUENCY (TF)
# ==========================================

def computeTF(wordDict, bagOfWords):

    tfDict = {}

    bagOfWordsCount = len(bagOfWords)

    for word, count in wordDict.items():

        tfDict[word] = count / float(bagOfWordsCount)

    return tfDict


tfA = computeTF(numOfWordsA, bagOfWordsA)

tfB = computeTF(numOfWordsB, bagOfWordsB)

print("\nTerm Frequency - Document A:")
print(tfA)

print("\nTerm Frequency - Document B:")
print(tfB)

# ==========================================
# STEP 12: COMPUTE INVERSE DOCUMENT FREQUENCY (IDF)
# ==========================================

def computeIDF(documents):

    N = len(documents)

    idfDict = dict.fromkeys(documents[0].keys(), 0)

    for document in documents:

        for word, val in document.items():

            if val > 0:

                idfDict[word] += 1

    for word, val in idfDict.items():

        idfDict[word] = math.log(N / float(val))

    return idfDict


idfs = computeIDF([numOfWordsA, numOfWordsB])

print("\nInverse Document Frequency:")
print(idfs)

# ==========================================
# STEP 13: COMPUTE TF-IDF
# ==========================================

def computeTFIDF(tfBagOfWords, idfs):

    tfidf = {}

    for word, val in tfBagOfWords.items():

        tfidf[word] = val * idfs[word]

    return tfidf


tfidfA = computeTFIDF(tfA, idfs)

tfidfB = computeTFIDF(tfB, idfs)

print("\nTF-IDF - Document A:")
print(tfidfA)

print("\nTF-IDF - Document B:")
print(tfidfB)

# ==========================================
# STEP 14: DISPLAY TF-IDF USING DATAFRAME
# ==========================================

df = pd.DataFrame([tfidfA, tfidfB])

print("\nFinal TF-IDF DataFrame:")

display(df)

# ==========================================
# PRACTICAL COMPLETED
# ==========================================

print("\nPractical 7 Completed Successfully!")
