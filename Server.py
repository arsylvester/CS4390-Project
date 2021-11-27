#Implement server code here. The following is example code from https://pymotw.com/2/socket/tcp.html

#Implement Client requester code here.
import socket
import sys
from theThreeFucntions import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listen for connections
sock.listen(1)

while True:
    #Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print>>sys.stderr, 'connection from', client_address

        #Recieve the data in small chunks and restransmit it
        while True:
            data = connection.recv(1000)
            print>>sys.stderr, 'received "%s"' % data
            if data:
                dataList = data.split()
                messageType = dataList[0]

                if(messageType == "GET"):
                    returnOrder(int(dataList[1]))
                    connection.sendall("Returning data")
                elif(messageType == "DEL"):
                    deleteFromList(dataList[1].lower(), 16)
                    connection.sendall(dataList[1].lower() + " has been deleted.")
                elif(messageType == "UPDATE"):
                    updateQuantity(dataList[1].lower(), 16, int(dataList[2]))
                    connection.sendall(dataList[1] + " Has been added")
                else:
                    #There is an error, return error
                    connection.sendall("ERROR: Can not process Header.")
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        #clean up connection
        connection.close()
