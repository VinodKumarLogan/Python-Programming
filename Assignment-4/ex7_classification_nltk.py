#from nltk.book import *
import nltk
from nltk.corpus import names
import random

def gender_features(word):
    return {'last_letter': word[-1]}

mynames = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(mynames)
#print mynames

featuresets = [(gender_features(n), g) for (n,g) in mynames]

train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print classifier.classify(gender_features(raw_input('enter name of a person: ')))
