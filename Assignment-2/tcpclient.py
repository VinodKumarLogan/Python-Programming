import sys
from socket import *

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
adminCount = 0
flag = True
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while flag:
	try:
		message = clientSocket.recv(1048576)
		if not not message:
			if 'Enter' in message:
				sendMsg = raw_input(message)
				clientSocket.send(sendMsg)
			elif message=='Exiting':
				print 'Done'
				flag = False
				break
			else:
				print message
				continue
		else:
			break
	except:
		break
clientSocket.close()