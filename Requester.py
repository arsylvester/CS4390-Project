#Requester.py: The client application that sends CTP messages to the server. Includes a simple text UI
# to help the user send CTP messages.
import socket
import sys

# These are the instructions AKA "user interface"
def printMessage():
    print ("\tCTP Test Case")

    print ("Command GET: (GET , *Order Flag)")
    print ("\t0 - Sort by Name")
    print ("\t1 - Sort by Qty")
    print ("\t2 - Sort by Date")
    print ("\tReturns: Sorted Database")

    print ("\nCommand DEL: (DEL , *Name of Item*)")
    print ("\tReturns: Response Acknowledgment - DACK")

    print ("\nCommand UPDATE: (UPDATE, *Name of Item*, *Quantity*)")
    print ("\tReturns: Response Acknowledgment - UACK")

    print ("\nExit anytime by entering 'q'")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
keepRunning = True

#Connect the socket to the port where the server is listening
server_address = (sys.argv[1], int(sys.argv[2]))
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

#Loop tell user says to quit
while(keepRunning):
    print("\n")
    printMessage()
    message = input("Enter Command: ")

    if message == "":
        print("\nNothing inputed, please try again.")
        continue
    
    if message == 'q':
        keepRunning = False
        sock.shutdown(socket.SHUT_WR)
        break

    try:
        #Send command
        print('\nSending "%s"' % message)
        sock.sendall(message.encode("utf-8"))

        #look for the response
        data = sock.recv(1024).decode()
        print('recieved "%s"\n' % data)

        #Split up CTP message to process
        dataList = data.split()
        messageType = dataList[0]

        #Check the message type and process accordingly   
        if(messageType == "RETURN"):
            #Prepare to recieve a file
            fileRecieved = open("RecievedFile.txt", "w")
            data = data[7:] #Ignore RETURN + space
            while(data):
                fileRecieved.write(data)
                data = sock.recv(1024).decode()
            fileRecieved.close()
        elif(messageType == "ERROR"): #Display to user type of error recieved.
            errorType = dataList[1]
            if(errorType == "0"):
                print('Message format issue. Please check that your header is correct.')
            elif(errorType == "1"):
                print('Name not found.')
            elif(errorType == "2"):
                print('Error occured on server end.')
    finally:
        sock.shutdown(socket.SHUT_WR)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
