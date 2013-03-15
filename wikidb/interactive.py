from wikidb import *
import sys
def interactive_menu():
	'''Interactive Menu Generator for the database'''
	db = None
	print 'Welcome to Database Server'
	while True:
		print 'Choose an option : '
		print '1. Create database '
		print '2. Select entries from database '
		print '3. Insert an entry into the database '
		print '4. Update an entry in the database '
		print '5. Delete an entry in the database '
		print '6. Exit '
		ch = raw_input()
		try:
			if int(ch) == 1:
				db =Database()
				fname = raw_input('Enter the file name : ')
				rnd = raw_input('Do you want to generate random entries (Y/n) : ')
				if rnd.lower() == 'y':
					nentries = int(raw_input('Enter number of entries : '))
					db.create(fname,nentries)
				if fname is None:
					print 'Error Please Enter again'
					continue
				db.create(fname)
				print 'Database Created'
				print 'Time taken = %s' % db.creattime
			elif int(ch) == 2:
				if db is None:
					print 'Please create database first'
					continue
				query = raw_input('Enter select query : \n')
				a = db.select(query)
				db.printdb(a)
				print 'Time taken for select = %2.5s s' % db.seltime
				print 'Time taken for printing = %2.5s s'%db.printtime
			elif int(ch) == 3:
				if db is None:
					print 'Please create database first'
					continue
				query = raw_input('Enter record to be inserted:\n')
				db.insert(query)
				print 'Inserted ',query, ' Successfully'
				print 'Time taken = %2.5s s' % db.instime
			elif int(ch) == 4:
				if db is None:
					print 'Please create database first'
					continue
				query = raw_input('Enter update query : \n')
				db.update(query)
				print 'Time taken = %2.5s s' % db.updtime
				print 'Updated all entries where ',query, ' Successfully'
			elif int(ch) == 5:
				if db is None:
					print 'Please create database first'
					continue
				query = raw_input('Enter delete query : \n')
				db.delete(query)
				print 'Deleted all entries where ',query, ' Successfully'
				print 'Time taken = %2.5s s' % db.deltime
			elif int(ch) == 6:
				print 'Bye'
				return
		except Exception as e:
			raise QuerySyntaxError('wrong syntax '+str(e))

