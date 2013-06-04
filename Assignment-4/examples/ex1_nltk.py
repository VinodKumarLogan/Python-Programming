from nltk.book import *

#look up for specific word - searching text
print text1.concordance('monstrous')
print '-----------------------------'
print text1.similar('monstrous')

print '-----------------------------'
print text2.similar('monstrous')

print text2.common_contexts(["monstrous", "very"])

#text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

print text8.generate()
"""
print '-----------------------------'
print text3.concordance('lived')
"""

#lexical richness

print 'lexical richness of text1 = ', float(len(text1)) / len(set(text1))
print 'type-token ratio of text1 = ', float(len(set(text1))) / len(text1)

#counting occurance of a given word in a text
myword = 'monstrous'
print 'The word %s occurs %s times in text1' % (myword, str(text1.count(myword)))
