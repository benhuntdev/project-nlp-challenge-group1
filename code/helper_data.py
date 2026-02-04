import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet


def load_data(filename, separator='\t'):
    return pd.read_csv(filename, sep=separator, header=None)

def display_data(data):
    print("Data head():")
    print(data.head())

    #print()
    #print("Data describe():")
    #print(data.describe())

    print()
    print("Data info():")
    print(data.info())

    print()
    print("Data shape:")
    print(data.shape)

# preprocessing: tokenize, lowercase, remove punctuation
def tokenizer_and_remove_punctuation(row, column):
    tokens = word_tokenize(row[column])
    return [word.lower() for word in tokens if word.isalpha()]

# apply stemming
def stemming(stemmer, row, column):
    return [stemmer.stem(word) for word in row[column]]

# unfortunately pos_tag and lemmatize use different codes for parts of speech
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper() # gets first letter of POS categorization
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN) # get returns second argument if first key does not exist

# apply lemmatization
def lemmatizer_with_pos(lemmatizer, row, column):
    return [lemmatizer.lemmatize(word,get_wordnet_pos(word)) for word in row[column]]

# remove stopwords
def remove_stopwords(stopwords, row, column):
  return list(set(row[column]).difference(stopwords.words()))

# concatenate text
def re_blob(row, column):
  return " ".join(row[column])