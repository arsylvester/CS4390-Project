#Server.py: The server code that will recieve the CTP messages and then interact with the database file.
# Will return ACK and ERROR messages to the client.
import socket
import sys
from theThreeFunctions import *

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
                #Split up CTP message to process it
                dataList = data.split()
                messageType = dataList[0]
                returnMessage = ""

                #Check the message type and process accordingly   
                if(messageType == "GET"):
                    #Check if header parameters are valid
                    if(len(dataList) > 1 and dataList[1].isdigit() and 0 <= int(dataList[1]) < 3):
                        returnOrder(int(dataList[1]))
                    else:
                        returnMessage = "ERROR 0"
                        connection.sendall(returnMessage.encode("utf-8"))
                        break
                    
                    #Prepare to send database file
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
                    #Check if header parameters are valid
                    if(len(dataList) <= 1):
                        returnMessage = "ERROR 0"
                        connection.sendall(returnMessage.encode("utf-8"))
                        break

                    #Check if name parameter is in the database
                    if(deleteFromList(dataList[1].lower(), len(DATABASE))):
                        returnMessage = "DACK " + dataList[1].lower()
                    else:
                        returnMessage = "ERROR 1"
                elif(messageType == "UPDATE"):
                    #Check if header parameters are valid
                    if(len(dataList) <= 2 or not dataList[2].isdigit()):
                        returnMessage = "ERROR 0"
                        connection.sendall(returnMessage.encode("utf-8"))
                        break
                    #Check if name parameter is in the database
                    if(updateQuantity(dataList[1].lower(), len(DATABASE), int(dataList[2]))):
                        returnMessage = "UACK " + dataList[1].lower() + " " + dataList[2]
                    else:
                        returnMessage = "ERROR 1"
                else:
                    #There is an error, return error
                    returnMessage = "ERROR 0"

                #Return message
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
