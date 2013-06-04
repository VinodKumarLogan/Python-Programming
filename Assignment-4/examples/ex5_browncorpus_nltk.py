#from nltk.book import *
import nltk
from nltk.corpus import brown

print nltk.corpus.brown.fileids()

"""
for fileid in brown.fileids():
    num_chars = len(brown.raw(fileid))
    num_words = len(brown.words(fileid))
    num_sents = len(brown.sents(fileid))
    num_vocab = len(set([w.lower() for w in brown.words(fileid)]))
    print num_chars, num_words, num_sents, num_vocab, fileid

"""

print brown.categories()
print brown.words(categories = 'news')
print brown.words(fileids = 'cg22')
print brown.sents(categories=['news', 'editorial', 'reviews'])

"""
The Brown Corpus is a convenient resource for studying systematic differences between
genres, a kind of linguistic inquiry known as stylistics. Let’s compare genres in their
usage of modal verbs. The first step is to produce the counts for a particular genre.
"""
news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print m + ':', fdist[m],

print '\n'
print '----------- adventure text --------------------------------------'
adventure_text = brown.words(categories='adventure')
fdist = nltk.FreqDist([w.lower() for w in adventure_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print m + ':', fdist[m],

print '\n'
print '----------- mystery text --------------------------------------'
mystery_text = brown.words(categories='mystery')
fdist = nltk.FreqDist([w.lower() for w in mystery_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print m + ':', fdist[m],

print '\n'
print '----------- religion text --------------------------------------'
religion_text = brown.words(categories='religion')
fdist = nltk.FreqDist([w.lower() for w in religion_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print m + ':', fdist[m],


raw_input('press enter to continue')

cfd = nltk.ConditionalFreqDist(
(genre, word)
for genre in brown.categories() for word in brown.words(categories=genre))

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']

cfd.tabulate(conditions=genres, samples=modals)

print 'conditions: ', cfd.conditions()
