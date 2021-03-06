import os
from collections import Counter

negativeReviews = []
positiveReviews = []
negativeWords = []
positiveWords = []
combinedWords = []
stopWords = ['is', 'a', 'of', 'the', 'it', 'and', 'for', 'with', 'be', 'in',
             'this', 'an', 'to', 'has', 'that', 'she', 'he', 'it', 'i', 'was',
             'as', 'are', 'on', 'his', 'her', 'at', 'have']


# This part scans trough all reviews of a certain folder and separates all words used into one list.

def positive_reviews(path):
    counter = 0
    for filename in os.listdir(path):
            try:
                if filename.endswith(".txt"):
                    positiveReviews.append(str(filename))
                    counter += 1
                    with open(path+filename, 'r', encoding='utf-8') as f:
                        for line in f:
                            for word in line.split():
                                if word.lower() not in stopWords:
                                    positiveWords.append(word)
            except Exception as e:
                raise e
                print("No files found!")
    print('In total', counter, 'positive reviews were scanned')
    return positiveWords


def negative_reviews(path):
    counter = 0
    for filename in os.listdir(path):
        try:
            if filename.endswith(".txt"):
                negativeReviews.append(str(filename))
                counter += 1
                with open(path + filename, 'r', encoding='utf-8') as f:
                    for line in f:
                        for word in line.split():
                            if word.lower() not in stopWords:
                                negativeWords.append(word)
        except Exception as e:
            raise e
            print("No files found!")
    print('In total', counter, 'negative reviews were scanned')
    return negativeWords


def word_frequency(listOfWords, top):
    listOfWords = Counter(listOfWords)
    listOfWords = listOfWords.most_common(top)
    return listOfWords




def word_probability_pos(word):
    for key, val in word_frequency(positiveWords, 1000):
        if key == word:
            print(key, val)
            occuranceNumber = val
    # probability of the word in the positive review
    probability = (occuranceNumber + 1) / (len(positiveWords)+len(combinedWords))
    return probability


positive_reviews('positive/')
print(word_frequency(positiveWords, 1000))
negative_reviews('negative/')
print(word_frequency(negativeWords, 1000))
print('Total positive words:',len(positiveWords))
print('Total negative words:',len(negativeWords))
combinedWords = positiveWords + negativeWords
print('Total unique words in all classes:',len(set(combinedWords)))

print(word_probability_pos('movie'))
