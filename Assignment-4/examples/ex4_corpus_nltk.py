#from nltk.book import *
import urllib
import nltk
from nltk.corpus import gutenberg
from nltk.corpus import webtext

print nltk.corpus.gutenberg.fileids()
words = nltk.corpus.gutenberg.words('austen-emma.txt')
print len(words)

ae = nltk.Text(words)
ae.concordance('surprize')

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print num_chars, num_words, num_sents, num_vocab, fileid

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
print macbeth_sentences[100]

longest_len = max([len(s) for s in macbeth_sentences])
print 'longest len: ', longest_len

print [s for s in macbeth_sentences if len(s) == longest_len]

for fileid in webtext.fileids():
    print fileid, webtext.raw(fileid)[:65], '...'
