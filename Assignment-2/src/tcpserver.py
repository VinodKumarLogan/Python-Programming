import sys, getopt,hashlib
from modes import *
from socket import *


def guestMode():
    ch = 'y'
    db = Database()
    printData = db.create()
    connSocket.send(printData)
    while ch=='y':
		connSocket.send('Enter your search query : ')
		query = connSocket.recv(1048576)
		p = db.select(query)
		printData = db.printdb(p)
		connSocket.send(printData)
		msg = 'Do you want to try another search query? (y/n) Enter your choice : '
		connSocket.send(msg)
		ch = connSocket.recv(1024)
		print ch

def adminMode():
    '''interactive menu generator for running 
    wikidb module '''
    c = 'y'
    db = Database()
    while c=='y':
        printData = ''
        printData =('#'*75)+'\n'
        printData+= ' 1. Create database \n'
        printData+= ' 2. Select entries from database \n'
        printData+= ' 3. Insert an entry into the database \n'
        printData+= ' 4. Update an entry in the database \n'
        printData+= ' 5. Delete an entry in the database \n'
        printData+= ' 6. Exit \n'
        printData+= '#'*75 + '\n'
        printData+= ' Enter an option : '
        connSocket.send(printData)
        ch = connSocket.recv(1024)
        printData = ''
        try:
            if int(ch) == 1:
                printData =  '\nIf the file you specify already exists the new entries will be\n appended to the file and original entries will be unchanged\n'
                printData =  'Enter the file name : '
                connSocket.send(printData)
                fname = connSocket.recv(1024)
                printData = ''
                printData = ' Do you want to generate random entries? Enter your choice (y/n):'
                connSocket.send(printData)
                rnd = connSocket.recv(1024)
                if rnd.lower() == 'y':
                    printData = 'Enter number of entries :'
                    connSocket.send(printData)
                    nentries = int(connSocket.recv(1024))
                    db.create(fname,nentries)
                else : 
                    printData = 'Creating database from entries already present in file \n'
                    connSocket.send(printData)
                if fname is None:
                    printData = 'Error Please Enter again\n'
                    connSocket.send(printData)
                    continue
                db = Database()
                db.create(fname)
                printData = ' Database Created in %s s'%db.creattime + '\n'
                connSocket.send(printData)
            elif int(ch) == 2:
                if db is None:
                    printData = ' Please create database first\n'
                    connSocket.send(printData)
                    continue
                printData = '''Syntax : <fields to be selected> where 
    condition(1) and/or condition(2) and/or 
    condition(3) ... condition(n).
    Here "and" has higher precedence than "or" '''
                connSocket.send(printData)
                printData = ' Enter select query : '
                connSocket.send(printData)
                query = connSocket.recv(4096)
                a = db.select(query)
                printData = db.printdb(a)
                connSocket.send(printData)
                printData = 'in %s s '%db.seltime + '\n'
                connSocket.send(printData)
            elif int(ch) == 3:
                if db is None:
                    printData = 'Please create database first\n'
                    connSocket.send(printData)
                    continue
                printData = 'Enter record to be inserted: \n'
                connSocket.send(printData)
                query = connSocket.recv(4096)
                if db.insert(fname,query):
                    printData = 'Inserted ',query,' Successfully in %s s'%db.instime + '\n'
                    connSocket.send(printData)
            elif int(ch) == 4:
                if db is None:
                    printData = 'Please create database first\n'
                    connSocket.send(printData)
                    continue
                printData = '''Update an entry in the database
    Syntax : <field(s) to be updated> where condition(1) 
    and/or condition(2) and/or condition(3) ... condition(n)'''
                connSocket.send(printData)
                printData='\nEnter update query : '
                connSocket.send(printData)
                query = connSocket.recv(4096)
                db.update(query)
                printData = 'Updated all entries where ',query, ' Successfully in %s s '%db.updtime + '\n'
                connSocket.send(printData)
            elif int(ch) == 5:
                if db is None:
                    printData = ' Please create database first\n'
                    connSocket.send(printData)
                    continue
                printData = '''Delete an entry from the database
    Syntax : where condition(1) and/or condition(2) and/or 
    condition(3)... condition(n)'''
                connSocket.send(printData)
                printData = ' Enter delete query : '
                connSocket.send(printData)
                query = connSocket.recv(4096)
                if db.delete(fname,query):
                    printData = 'Deleted all entries where ',query, ' Successfully in %s s '%db.deltime + '\n'
                    connSocket.send(printData)
            elif int(ch) == 6:
                printData = 'Bye\n'
                connSocket.send(printData)
                c = 'n'
                return
        except :
            printData = 'Wrong Syntax\n'
            connSocket.send(printData)



salt = 'Js,<>qwm?/a"8123]w@)inad80BJBd'
serverName = '127.0.0.1'
serverPort = int(sys.argv[1])

password = 'hawkeye'
m = hashlib.md5()
p = m.update(salt+password)
pcheck = m.hexdigest()
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
adminCount = 0
print "Database Server Has Started"
flag = True
connSocket, clientAddr = serverSocket.accept()
while flag:
    choice = '\nWelcome to Database Server \nEnter your choice :-\n1.Administrator\n2.Guest\n3.Exit\n'
    connSocket.send(choice)
    ch = connSocket.recv(1048576)
    print ch
    if ch=='1':
        if adminCount<=2:
            message = 'Enter the password: '
            connSocket.send(message)
            recdMessage = connSocket.recv(1048576)
            print recdMessage
            t = hashlib.md5()
            resMsg = t.update(salt+recdMessage)
            resMsg = t.hexdigest()
            if resMsg==pcheck:
                print 'Good'
                connSocket.send('Authentication Successful')
                adminMode()
                adminCount = 0
                flag = True
            else:
                adminCount+=1
                connSocket.send('Authentication Failed. Try again')
                if adminCount>2:
    				flag = False
    				print 'sent'
    				connSocket.send('Exiting')
    				break
    	else:
    		flag = False
    		connSocket.send('Exiting')
    elif ch=='2':
    	connSocket.send('Guest mode Activated')
    	guestMode()
    	flag = True
    elif ch=='3':
    	connSocket.send('Exiting')
    	flag = False
    else:
    	connSocket.send('Invalid Option. Please try again.')
    	continue
#connSocket.close()