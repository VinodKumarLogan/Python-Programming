#from nltk.book import *
import urllib
import nltk

myurl = r'c:\home\ananth\research\python\pesit\unit5\datasets\mobile.txt'

f = open(myurl)
txt = f.read()

toks = txt.split()
print nltk.bigrams(toks)

txt1 = nltk.Text(toks)
#print txt1.generate()
txt1.collocations()
