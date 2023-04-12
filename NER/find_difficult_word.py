import textstat
import pyphen
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# def find_difficult_words(sentence, age_range=(10, 16)):
#     # Calculate the FKGL score of the sentence
#     fkgl_score = textstat.flesch_kincaid_grade(sentence)

#     # Extract the lower and upper age range
#     lower_age, upper_age = age_range

#     # Find the target grade level range
#     target_lower_grade =0  # Formula to calculate target lower grade level
#     target_upper_grade = 15  # Formula to calculate target upper grade level

#     # Find words with syllable count greater than the target upper grade level
#     difficult_words = []
#     words = sentence.split()
#     for word in words:
#         syllable_count = textstat.syllable_count(word)
#         word_grade = textstat.flesch_kincaid_grade(word)
#         if syllable_count > target_upper_grade and word_grade > target_upper_grade:
#             difficult_words.append(word)

#     return difficult_words


def find_difficult_words(sentence):
    # Create an instance of Pyphen for English language
    dic = pyphen.Pyphen(lang='en')

    # Tokenize the sentence into words
    words = sentence.split()

    # Extract words with more than one syllable
    difficult_words = [word for word in words if len(dic.inserted(word).split('-')) > 1]
    
    

    return difficult_words

def find_nouns(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Perform part-of-speech (POS) tagging on the words
    pos_tags = nltk.pos_tag(words)

    # Extract proper nouns and common nouns from the POS tags
    proper_nouns = []

    for word, pos in pos_tags:
        if pos == 'NNP':
            proper_nouns.append(word)
        # elif pos in ['NN', 'NNS']:
        #     common_nouns.append(word)

    return proper_nouns



def get_tough_words(sentence):
    difficult_words = find_difficult_words(sentence)
    proper_nouns = find_nouns(sentence)
    
    return  list(set(difficult_words + proper_nouns))
    
    
# Example usage:
sentence = "The boy was eating a mango. Ramu loves cat. Banana's should be eaten daily."
difficult_words = find_nouns(sentence)
print("Difficult words:", difficult_words)
# Example usage:
sentence = "he ate an apple because he was hungry and abject"
difficult_words = find_difficult_words(sentence)
print("Difficult words:", difficult_words)