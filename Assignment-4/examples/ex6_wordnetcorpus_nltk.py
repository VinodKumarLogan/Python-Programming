#from nltk.book import *
import nltk
from nltk.corpus import wordnet as wn


"""
WordNet is a semantically oriented dictionary of English, similar to a traditional thesaurus
but with a richer structure. NLTK includes the English WordNet, with 155,287
words and 117,659 synonym sets.
"""

print wn.fileids()

w = raw_input('enter a word: \t\t')
syns = wn.synsets(w)

for syn in syns:
    print syn.lemma_names, ':\t', syn.definition
    mytypes = syn.hyponyms()
    mytypes1 = syn.hypernyms()
    print 'length of hyponyms: ', len(mytypes)
    print mytypes[0]
    print sorted([lemma.name for synset in mytypes for lemma in synset.lemmas])
    print sorted([lemma.name for synset in mytypes1 for lemma in synset.lemmas])





"""
for fileid in wn.fileids():
    num_chars = len(wn.raw(fileid))
    num_words = len(wn.words(fileid))
    num_sents = len(wn.sents(fileid))
    num_vocab = len(set([w.lower() for w in wn.words(fileid)]))
    print num_chars, num_words, num_sents, num_vocab, fileid

"""
