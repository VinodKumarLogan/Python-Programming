html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
import urllib2

soup = BeautifulSoup(html_doc)

print(soup.prettify())

raw_input('Enter a key to continue')

print '--------------------------------------------------------------------'
print soup.title
# <title>The Dormouse's story</title>

print soup.title.name
# u'title'

#print soup.title.string
# u'The Dormouse's story'

print soup.title.parent.name
# u'head'

print soup.p
# <p class="title"><b>The Dormouse's story</b></p>

print soup.p['class']
# u'title'

print soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

raw_input('Enter a key to continue')

#One common task is extracting all the URLs found within a page�s <a> tags:

for link in soup.find_all('a'):
    print(link.get('href'))

raw_input('Enter a key to continue')

print (soup.get_text())

raw_input('Enter a key to continue')

soup = BeautifulSoup(open(r'c:\temp\example.xml'))
print soup.prettify()

raw_input('Enter a key to continue - get_text')
print soup.get_text()

raw_input('Enter a key to continue')

soup = BeautifulSoup(urllib2.urlopen('http://www.adobe.com'))
print soup.prettify()

raw_input('Enter a key to continue - all hyperlinks')
links = soup.find_all('a')
print len(links)

for link in links:
    h = link.get('href')
    if (h != None):
        print h
