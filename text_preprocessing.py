import numpy as np 
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import re
# nltk.download('stopwords')
stop_words = stopwords.words('english')
# import re
st = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def lemmatize(sentence, remove_stopwords= True):
    """
    It will take the word and covert it to its meanigfull format
    finally  final finale finalized ---> 
    """
    if remove_stopwords:
        return   " ".join([lemmatizer.lemmatize(word)for word in sentence.split() if word not in stop_words])
    else:
        return   " ".join([lemmatizer.lemmatize(word)for word in sentence.split()])
        
    
def stemm(sentence, remove_stopwords = True):
    """
    It will add some AIness to the code 
    That is, 
    it will consider the words like [hello, hi, hey] in the same way
    eg - it will convert
    ["Final ", "Finalized", "Finally", "finale"]
    to [Final] because it is common in all the words, rest all is considered as the suffix and is exploited
    """
    if remove_stopwords:
        return  " ".join([st.stem(word) for word in sentence.split() if word not in stop_words])
    else:
        return  " ".join([st.stem(word) for word in sentence.split() ])

def preprocessing(sentence, lemma = True, stemm = False, remove_stopwords = True, numbers  = True, lower = True):
   ######################### Preprocessing for new_data ##########################e
   
    if lower:
        sentence = sentence.lower()
    #line break removal
    sentence = re.sub(r"\r?\\n"," ", sentence)
    #remove special characters
    sentence = re.sub(r'\W+', ' ', sentence)
    if numbers:
    #remove numbers
        sentence = sentence.replace('\d+', '')
        sentence = re.sub(r'\b\d+\b', ' ', sentence)
    #remove punctuation
    sentence = sentence.replace('[^\w\s]','')
    #remove underscore
    sentence = sentence.replace('_', '')

    if lemma:
        sentence = lemmatize(sentence, remove_stopwords)
    if stemm:
        sentence = stemm(sentence, remove_stopwords)
    

    return sentence

if __name__ == '__main__':
    print(preprocessing("What is the sum of 2 & 2 _ _ ?", numbers=False)) 