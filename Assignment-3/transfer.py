from pymongo import *
client = MongoClient('localhost',27017)
db = client.WikiPeopleDatabase
wikipeople = db.WikiPeopleDatabase
f = open('test.db','r')
t = f.readline().split(';')[:-1]
for p in t:
	entry = {}
	l = p.split(',')
	for k in l:
		y = k.split('=')
		print y
		entry[y[0]] = y[1]
	wikipeople.insert(entry)