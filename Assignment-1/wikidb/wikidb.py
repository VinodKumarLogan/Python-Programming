#!/usr/bin/python
from argparse import ArgumentParser
import string
import random 
import os
import sys
from time import *

def id_generator(chars=string.ascii_lowercase):
	'''Generates random strings of random length'''
	size = random.randrange(4,6)
	return ''.join(random.choice(chars) for x in range(size))

def gen_rand_data(datarange,database,fname='test.db'):
	'''Generates random entries for the database'''
	i = 0
	f = open(fname,'a')
	while i<datarange:
		e = {}
		name = str(id_generator())+ ' ' +str(id_generator())
		year = random.randrange(1990,2013)
		category = random.choice(['Peace','Physics','Chemistry','Literature','Economics'])
		achievement = str(id_generator()).strip()
		gender = random.choice(['m','f'])
		country = random.choice(['India','Germany','France','USA','England','China','Russia','Switzerland'])
		e['name'] = name.strip()
		e['year'] = year
		e['category'] = category.strip()
		e['achievement'] = achievement
		e['gender'] = gender
		e['country'] = country.strip()
		f.write("name="+name+",year="+str(year)+",category="+category+",achievement="+achievement+",gender="+gender+",country="+country+";")
		database.append(e)
		i = i + 1
	return database

class QuerySyntaxError(Exception):
	''' Class for syntax error in queries'''
	def __init__(self,message,errormsg='Error'):
		Exception.__init__(self,message)
		self.errormsg = errormsg
		self.usage()
	def usage(self):
		print '''
		usage: wikidb.py [-h] [-i --insert] [-u --update] [-d --delete]
                 [-f --filename] [-g --generate] [-s --select] [--interactive]

		optional arguments:
  			-h, --help     show this help message and exit
  			-i --insert    Insert entries into the database
  			-u --update    Update the entries in the database
  			-d --delete    Delete an entry in database
  			-f --filename  Filename which contains the database
  			-g --generate  Generates the random entries for the database
  			-s --select    Select particular entries from database
  			--interactive  Run in interactive mode
		'''
		
class Database:
	def __init__(self):
		self.seltime = 0
		self.printtime = 0
		self.creattime = 0
		self.deltime = 0
		self.updtime = 0
		self.instime = 0
	'''Class for database operations'''
	def serialize(self):
		'''Convert the database object to
		strings for storing in file'''
		dbstr = ''
		for i in self.maindb:
			tstr = ''
			for j in i.keys():
				tstr += j+'='+str(i.get(j,''))+','
			dbstr += tstr[:-1]+';'
		return dbstr

	def printdb(self,p=None):
		'''Print the database or the results
		in suitable format'''
		start = time()
		if p is None:
			print 'NULL'
			return
		keysstr = ''
		if p==[]:
			print 'NULL'
			return
		print '='*100
		for j in p[0]:
			keysstr += '%10s'%j + ' '*9
		print keysstr
		print '='*100
		for j in p: 
			astr = ''
			for k in j.keys(): 
				astr += '%12s'%j.get(k,'')+' '*5
			print astr
		print '='*100
		print 'Fetched %s entrie(s)'%(str(len(p)))
		self.printtime = time() - start

	def create(self,fname,rnumber=0):
		'''Read from existing db file and create 
		the database.Also create database using 
		random entries'''
		now = time()
		self.dbstr=''
		self.maindb=[]
		maindb = self.maindb
		
		if os.path.exists(fname) and os.stat(fname)[6] != 0:
			try:
	   			dbfile = open(fname)
	   		except IOError as ie:
	   			print 'IOError occured'
	   			return
			datastr = dbfile.read()
			datastr.strip('\n')
			maindb = datastr.split(';');
			for i in range(0,len(maindb)):
				maindb[i] =  maindb[i].split(',')
			for i in range(0,len(maindb)):
				t = {}
				tdbstr = ''
				for k in maindb[i]:
					temp = k.split('=')
					if len(temp)==2:
						t[temp[0]]=temp[1]
				if t.keys() == []:
					continue
				maindb[i] = t
			del(maindb[-1])
			dbfile.close()
		self.maindb= maindb
		if rnumber != 0:
			for x in gen_rand_data(rnumber,[],fname):
				if type(x) != dict:
					continue
				self.maindb.append(x)
		self.creattime = time()-now
	def insert(self,qstr):
		'''Insert a record into the database
		Syntax : field(1)=value(1),field(2)=value(2)...field(n)=value(n);'''
		start = time()
		maindb = self.maindb
		b = qstr.split(';')[0].split(',')
		temp = ''
		for x in b:
			d = {}
			c = x.split('=')
			if c[0].lower() == 'name':
				d['name'] = c[1]
				temp += 'name='+c[1]+','
			elif c[0].lower() == 'year': 
				d['year'] = c[1]
				temp += 'year='+c[1]+','
			elif c[0].lower() == 'category':
				d['category'] = c[1]
				temp += 'category='+c[1]+','
			elif c[0].lower() == 'gender':
				d['gender'] = c[1]
				temp += 'gender='+c[1]+','
			elif c[0].lower() == 'acheivement':
				d['achievement'] = c[1]
				temp += 'achievement='+c[1]+','
			elif c[0].lower() == 'country':
				d['country'] = c[1]
				temp += 'country='+c[1]+','
			maindb.append(d)
		f = open('test.db','a')
		te = temp[:-1]+';'
		f.write(te)
		f.close()
		self.instime =time() - start
	def project(self,proj,tresult):
		'''Returns projection onto specified 
		fields'''
		proj = proj.strip()
		if proj.lower() == 'all' or proj== '*':
			return tresult
		else:
			result = []
			projli = proj.split(',')
			for i in tresult:
				p = {}
				for j in projli: 
					p[j]=i.get(j,None)
				result.append(p)
			return result

	def select(self,query):
		'''Select entries from the database.
		Syntax : <fields to be selected> where 
		condition(1) and/or condition(2) and/or 
		condition(3) ... condition(n).
		Here "and" has higher precedence than "or" '''
		start = time()
		self.seltime = ''
		query = query.lower()
		try : 
			if query.find('where') == -1:
				if query.strip() == 'all' or query.strip() == '*':
					self.seltime = time() - start
					return self.maindb
				else:
					print 'Wrong syntax'
					self.seltime = time() - start
					return []
			qlist = query.split('where')
			projstr = qlist[0]
			if qlist[1].strip(' ') == 'all' or qlist[1].strip() =='*':
				result = self.project(projstr,self.maindb)
				self.seltime = time() - start
				return result
			qlist = qlist[1].split(' or ')
			tresult = []		
			for j in qlist:
				temp = {}
				if j.find(' and ') == -1:
					j = j.strip()
					if j.find('!=') != -1:
						j = j.split('!=')
						for p in self.maindb:
							for k in p.keys():
								if j[0] == k:
									break
							if j[1] != p.get(j[0],None).lower():
								tresult.append(p)
					else:
						j = j.split('=')
						for p in self.maindb:
							for k in p.keys():
								if j[0] == k:
									break
							if j[1] == p.get(j[0],None).lower():
								tresult.append(p)

				else:
					andlist = j.split(' and ')
					for n in self.maindb:
						cnt = 0
						for ae in andlist:
							for be in andlist:
								ae = ae.strip()
								be = be.strip()
								if ae != be:
									cnt += 1
									if ae.find('!=') != -1:
										al = ae.split('!=')
										if be.find('!=') != -1:
											bl = be.split('!=')
											if al[1] != n.get(al[0],None).lower() and bl[1] != n.get(bl[0],None).lower():
												cnt -= 1
										else:
											bl = be.split('=')
											if al[1] != n.get(al[0],None).lower() and bl[1] == n.get(bl[0],None).lower():
												cnt -= 1
									else:
										al = ae.split('=')
										if be.find('!=') != -1:
											bl = be.split('!=')
											if al[1]== n.get(al[0],None).lower() and bl[1] != n.get(bl[0],None).lower():
												cnt -= 1
										else:
											bl = be.split('=')
											if al[1] == n.get(al[0],None).lower() and bl[1]== n.get(bl[0],None).lower():
												cnt -= 1

						if cnt == 0:
							if n not in tresult:
								tresult.append(n)
			if tresult == []:
				return [] 
			result = self.project(projstr,tresult)
			self.seltime = time() - start
			return result
		except :
			raise
			#raise QuerySyntaxError('wrong syntax')


	def update(self,qstr,fname):
		'''Update an entry in the database
		Syntax : <field(s) to be updated> where condition(1) 
		and/or condition(2) and/or condition(3) ... condition(n)'''
		start = time()
		qstr = qstr.lower()
		qupdate = qstr.split('where')
		selected = self.select('all where '+qupdate[1])
		qupdate = qupdate[0].strip()
		qupdate = qupdate.split(',')
		for i in qupdate:
			j = i.split('=')
			p = {}
			if j[0].lower() == "name":
				for k in selected:
					p['name'] = j[1]
					p['category'] = k['category']
					p['country'] = k['country']
					p['year'] = k['year']
					p['gender'] = k['gender']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == "year":
				for k in selected:
					p['year'] = j[1]
					p['category'] = k['category']
					p['country'] = k['country']
					p['name'] = k['name']
					p['gender'] = k['gender']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == "gender":
				for k in selected:
					p['gender'] = j[1]
					p['category'] = k['category']
					p['country'] = k['country']
					p['year'] = k['year']
					p['name'] = k['name']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == "category":
				for k in selected:
					p['category'] = j[1]			
					p['name'] = k['name']
					p['country'] = k['country']
					p['year'] = k['year']
					p['gender'] = k['gender']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == "country":
				for k in selected:
					p['country'] = j[1]
					p['name'] = k['name']
					p['country'] = k['country']
					p['year'] = k['year']
					p['gender'] = k['gender']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			f = open(fname,"w")
			st = self.serialize()
			f.write(st)
			f.close()
			self.updtime = time() - start

	def delete(self,qdel,fname):
		'''Delete an entry from the database
		Syntax : where condition(1) and/or condition(2) and/or 
		condition(3)... condition(n)'''
		start = time()
		self.maindb = {}
		self.dbstr = ''
		qdel =qdel.strip('where')
		tobedel = self.select('* where '+qdel)
		try:
			for j in tobedel:
				del(self.maindb[self.maindb.index(j)])
			st = self.serialize()
			f = open(fname,'w')
			f.write(st)
			f.close()
			self.deltime = time() -start
		except IOError as ie :
			print 'IOError occuered'
		except:
			raise QuerySyntaxError('wrong syntax')

def main():
	argparser = ArgumentParser()
	argparser.add_argument("-i",metavar="--insert",help="Insert entries into the database",default=None,type=str)
	argparser.add_argument("-u",metavar="--update",help="Update the entries in the database",default=None,type=str)
	argparser.add_argument("-d",metavar="--delete",help="Delete an entry in database",default=None,type=str)
	argparser.add_argument("-f",metavar="--filename",help="Filename which contains the database",default=None,type=str)
	argparser.add_argument('-g',metavar='--generate',help="Generates the random entries for the database",default=None,type=int)
	argparser.add_argument("-s",metavar="--select",help="Select particular entries from database",default=None,type=str)
	argparser.add_argument("--interactive",action='store_true',help="Run in interactive mode")
	args = argparser.parse_args()

	if args.interactive:
		try:
			 import interactive 
		except ImportError as ie:
			print 'ImportError ',ie
			sys.exit(1)
		interactive.interactive_menu()
		sys.exit(0)
	db = Database()
	if args.f:
		fname = args.f
	else:
		fname = 'test.db'
	if args.g:
		db.create(fname,args.g)
		print 'Generated %s random records'%(str(args.g))
		print 'Time taken for creation %2.5s s ' % db.creattime
	else:
		db.create(fname)
		print 'Time taken for creation %2.5s s ' % db.creattime
	if args.s :
		p = db.select(args.s)
		db.printdb(p)
		print 'Time taken for select %2.5s s '% db.seltime
		print 'Time taken for print %2.5s s' % db.printtime
	if args.i:
		db.insert(args.i)
		print 'Time taken for insert %2.5s' % db.instime
	if args.d:
		db.delete(args.d,fname)
		print 'Time taken for delete %2.5s' % db.deltime
	if args.u:
		db.update(args.u,fname)
		print 'Time taken for update %2.5s' % db.updtime
if __name__ == '__main__':
	t = time()
	main()
