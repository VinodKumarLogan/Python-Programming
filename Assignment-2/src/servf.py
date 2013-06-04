#!/usr/bin/python
#TCP server program
import sys
import hashlib
import logger
from socket import *
from modes import *
from threading import Thread
from datetime import date
from argparse import ArgumentParser

def guestMode(connSocket,addr,log,db):
    '''Serves for guests'''
    #global log
    ch = 'y'
    printData = db.create()
    try:
        connSocket.send(printData)
        while ch=='y':
            connSocket.send('Enter your search query : ')
            query = connSocket.recv(1048576)
            log.write(str(time.now())+'Query '+query+'received from '+str(addr)+"\n")
            p = db.select(query)
            printData = db.printdb(p)
            connSocket.send(printData)
            msg = 'Do you want to try another search query? (y/n) Enter your choice : '
            connSocket.send(msg)
            ch = connSocket.recv(1024)
            print ch  
    
    except error,message:
        if message != '[Error 32 Broken Pipe]':
            printData = 'Wrong Syntax\n'
            connSocket.send(printData)
        else:
            log.write(str(time.now())+' Client '+str(addr)+' exited abruptly\n')
        sys.exit(1)

def adminMode(connSocket,addr,log,db):
    '''interactive menu generator for running 
    wikidb module '''

    #global log
    c = 'y'
    printData = db.create()
    try:
        while c=='y':
            printData = ''
            printData =('#'*75)+'\n'
            printData += ' 1. Create database \n'
            printData += ' 2. Select entries from database \n'
            printData += ' 3. Insert an entry into the database \n'
            printData += ' 4. Update an entry in the database \n'
            printData += ' 5. Delete an entry in the database \n'
            printData += ' 6. Exit \n'
            printData += '#'*75 + '\n'
            printData += ' Enter an option : '
            connSocket.send(printData)
            ch = connSocket.recv(1024)
            log.write(str(time.now())+'Query '+ch+'received from '+str(addr)+'working in admin mode\n')
            printData = ''
            if int(ch) == 1:
                printData =  '\nIf the file you specify already exists the new entries will be\n appended to the file and original entries will be unchanged\n'
                printData =  'Enter the file name : '
                connSocket.send(printData)
                fname = connSocket.recv(1024)
                if fname is None:
                    printData = 'Error Please Enter again\n'
                    connSocket.send(printData)
                    continue
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
                query = connSocket.recv(1048576)
                print query
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
    except error,message:
        if message != '[Error 32 Broken Pipe]':
            printData = 'Wrong Syntax\n'
            connSocket.send(printData)
        else:
            log.write(str(time.now())+' Client '+str(addr)+' exited abruptly\n')
        sys.exit(1)
    except:
        printdat =  'Wrong syntax\n'
        childSocket.send(printdat)
        sys.exit(1)


def handle_child(childSocket, childAddr,log):
    '''Thread to handle tcp requests'''

    #global log
    t = open("password","r")
    tpass = t.readline().split(" ")
    password = tpass[0]
    m = hashlib.md5()
    salt = tpass[1]
    t.close()
    p = m.update(salt+password)
    pcheck = m.hexdigest()
    db = Database()
    running = True
    adminCount = 0
    clientSocket = childSocket
    try:
        while running:
            choice = '\nWelcome to Database Server \nEnter your choice :-\n1.Administrator\n2.Guest\n3.Exit\n'
            clientSocket.send(choice)
            ch = clientSocket.recv(1048576)
            if ch==1:
                log.write(str(time.now())+' Serving '+str(childAddr)+' as admin\n')
            else:
                log.write(str(time.now())+' Serving '+str(childAddr)+' as guest\n')
            print ch
            if ch=='1':
                if adminCount<=2:
                    message = 'Enter the password: '
                    clientSocket.send(message)
                    recdMessage = clientSocket.recv(1048576)
                    print recdMessage
                    log.write(str(time.now())+'Recievd password from '+str(childAddr)+'(working in admin mode)\n')
                    t = hashlib.md5()
                    resMsg = t.update(salt+recdMessage)
                    resMsg = t.hexdigest()
                    if resMsg==pcheck:
                        print 'Good'
                        log.write(str(time.now())+'Authentication Successful '+str(childAddr)+' now granted admin access\n')
                        clientSocket.send('Authentication Successful')
                        adminMode(clientSocket,childAddr,log,db)
                        adminCount = 0
                        flag = True
                    else:
                        adminCount+=1
                        log.write(str(time.now())+'Three unsuccessful password attempts for admin by'+str(childAddr)+"\n")
                        clientSocket.send('Authentication Failed. Try again\n')
                        if adminCount>2:
                            print 'sent'
                            clientSocket.send('Exiting\n')
                            running = False
                            break
                else:
                    running = False
                    log.write(str(time.now())+str(childAddr)+ ' chose to end connection\n')
                    clientSocket.send('Exiting')
            elif ch=='2':
                clientSocket.send('Guest mode Activated')
                guestMode(clientSocket,childAddr,log,db)
                flag = True
            elif ch=='3':
                clientSocket.send('Exiting')
                running = False
            else:
                clientSocket.send('Invalid Option. Please try again.')
                continue
    except error,message:
        if message != '[Error 32 Broken Pipe]':
            printData = 'Wrong Syntax\n'
            connSocket.send(printData)
        else:
            log.write(str(time.now())+' Client '+str(addr)+' exited abruptly\n')
        sys.exit(1)
    except:
        printdat =  'Wrong syntax\n'
        childSocket.send(printdat)
        sys.exit(1)
    childSocket.close()
    print "Child thread completed\n"

def main(log):
    '''Runs the database server'''

    #global log
    parser = ArgumentParser()
    parser.add_argument('-s',metavar='host',help='host name on which server runs')
    parser.add_argument('-p',metavar='port',help='port on which server runs')
    args = parser.parse_args()
    if not args.s or not args.p :
        print 'Error : Invalid command line args'
        print '''usage: servf.py [-h] [-s host] [-p port]

optional arguments:
  -h, --help  show this help message and exit
  -s host     host name on which server runs
  -p port     port on which server runs
        '''
        sys.exit(1)
    serverName = args.s
    try:
        serverPort = int(args.p)
    except:
        print 'Error : Port number has to be an integer'
        sys.exit(1)

    try:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', serverPort))
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSocket.listen(5)
    except:
        print 'Error : Unable to create socket(This is probabaly because a previous socket created on this \
            port was not closed properly)'
        sys.exit(1)
    #log = logger.Logger('serverlogfile.log')
    log.write(str(time.now())+'Server started on host '+args.s+' port '+args.p+"\n")
    print "TCP Server ready to receive data"
    while 1:
        try:
            connSocket, clientAddr = serverSocket.accept()
            log.write(str(time.now())+'Accepted connection from '+str(clientAddr)+'\n')
            t = Thread(target=handle_child,
                        args=(connSocket, clientAddr,log))
            t.start()
        except KeyboardInterrupt:
            log.write(str(time.now())+'Server stopped')
            print 'Server stopped'
            break

fileName = "../logs/log_"+str(date.today())+".log"
log = open(fileName,"a")
log.write(str(time.now()))
if __name__=="__main__":
    main(log)
log.close()