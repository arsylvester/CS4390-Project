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
                    if(len(dataList) > 1 and dataList[1].isdigit() and 0 <= int(dataList[1]) < 3):
                        returnOrder(int(dataList[1]))
                    else:
                        returnMessage = "ERROR 0"
                        connection.sendall(returnMessage.encode("utf-8"))
                        break
                    fileToSend = open('Database.txt')
                    
                    returnMessage = "RETURN " + fileToSend.read(1024)
                    connection.sendall(returnMessage.encode("utf-8"))
                    leftToSend = fileToSend.read(1024)
                    #If anything left in file make sure to send
                    while(leftToSend):
                        leftToSend = fileToSend.read(1024)
                        connection.sendall(leftToSend.encode("utf-8"))
                    fileToSend.close()
                    break
                elif(messageType == "DEL"):
                    if(len(dataList) <= 1):
                        returnMessage = "ERROR 0"
                        connection.sendall(returnMessage.encode("utf-8"))
                        break
                    if(deleteFromList(dataList[1].lower(), len(DATABASE))):
                        returnMessage = "DACK " + dataList[1].lower()
                    else:
                        returnMessage = "ERROR 1"
                elif(messageType == "UPDATE"):
                    if(len(dataList) <= 2 or not dataList[2].isdigit()):
                        returnMessage = "ERROR 0"
                        connection.sendall(returnMessage.encode("utf-8"))
                        break
                    if(updateQuantity(dataList[1].lower(), len(DATABASE), int(dataList[2]))):
                        returnMessage = "UACK " + dataList[1].lower() + " " + dataList[2]
                    else:
                        returnMessage = "ERROR 1"
                else:
                    #There is an error, return error
                    returnMessage = "ERROR 0"

                connection.sendall(returnMessage.encode("utf-8"))
            else:
                print('no more data from', client_address)
                break
    except:
        returnMessage = "ERROR 2"
        connection.sendall(returnMessage.encode("utf-8"))
    finally:
        #clean up connection
        connection.close()
