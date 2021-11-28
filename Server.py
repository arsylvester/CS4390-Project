#Implement server code here. The following is example code from https://pymotw.com/2/socket/tcp.html

#Implement Client requester code here.
import socket
import sys
from theThreeFucntions import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = (sys.argv[1], int(sys.argv[2]))
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

#listen for connections
sock.listen()

while True:
    #Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        #Recieve the data in small chunks and restransmit it
        while True:
            data = connection.recv(1024).decode()
            print('received "%s"' % data)
            if data:
                dataList = data.split()
                messageType = dataList[0]
                returnMessage = ""

                if(messageType == "GET"):
                    returnOrder(int(dataList[1]))
                    fileToSend = open('Database.txt')
                    
                    returnMessage = "RETURN \n\n" + fileToSend.read(1024)
                    connection.sendall(returnMessage.encode("utf-8"))
                    leftToSend = fileToSend.read(1024)
                    #If anything left in file make sure to send
                    while(leftToSend):
                        leftToSend = fileToSend.read(1024)
                        connection.sendall(leftToSend.encode("utf-8"))
                    fileToSend.close()
                    break
                elif(messageType == "DEL"):
                    deleteFromList(dataList[1].lower(), len(DATABASE))
                    returnMessage = "DACK " + dataList[1].lower()
                elif(messageType == "UPDATE"):
                    updateQuantity(dataList[1].lower(), len(DATABASE), int(dataList[2]))
                    returnMessage = "UACK " + dataList[1].lower() + " " + dataList[2]
                else:
                    #There is an error, return error
                    returnMessage = "ERROR: Can not process Header."

                connection.sendall(returnMessage.encode("utf-8"))
                fileToSend.close()
            else:
                print('no more data from', client_address)
                break
    finally:
        #clean up connection
        connection.close()
