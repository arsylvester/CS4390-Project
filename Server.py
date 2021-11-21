#Implement server code here.

#The following is code used from Assignment 2
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
port = 9000
serverSocket.bind(('', port))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024) 
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() 
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send('\nHTTP/1.1 404 NOT FOUND\n\n')
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()