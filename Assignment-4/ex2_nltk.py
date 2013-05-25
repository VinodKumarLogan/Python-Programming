from nltk.book import *
import urllib
import nltk

myurl = 'http://techcrunch.com/startups/'

fdist1 = FreqDist(text1)
vocab1 = fdist1.keys()
values = fdist1.values()
items = fdist1.items()

print 'Vocabulary of text1 has ', len(vocab1), ' words'

for i in range(50):
    print vocab1[i], '\t', values[i]


f1 = urllib.urlopen(myurl)
html = f1.read()
txt = nltk.clean_html(html)

#content = nltk.Text(txt.split())
content = nltk.Text(nltk.word_tokenize(txt))


fdist1 = FreqDist(content)
vocab1 = fdist1.keys()
values = fdist1.values()
items = fdist1.items()

print 'Vocabulary of text1 has ', len(vocab1), ' words'

for i in range(50):
    print vocab1[i], '\t', values[i]

print fdist1.hapaxes()
fdist1.plot(50, cumulative = False)

"""
a. {w | w ∈ V & P(w)}
b. [w for w in V if p(w)]
"""

V = set(text1)
long_words = [w for w in V if len(w) > 15]
print sorted(long_words)
