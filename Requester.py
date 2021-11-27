#Implement Client requester code here. The following is example code from https://pymotw.com/2/socket/tcp.html
import socket
import sys

# These are the instructions AKA "user interface"
def printMessage():
    print ("\tCTP Test Case")

    print ("Command GET: (GET , *Order Flag)")
    print ("\t0 - No Order")
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

while(keepRunning):
    print("\n")
    printMessage()
    message = input("Enter Command: ")
    
    if message == 'q':
        keepRunning = False

    try:
        #Send command
        print('Sending "%s"' % message)
        sock.sendall(message.encode("utf-8"))

        #look for the response
        amount_received = 0
        #what is this???
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(1000)
            amount_received += len(data)
            print('recieved "%s"' % data)
    finally:
        print('closing socket')
        sock.shutdown(socket.SHUT_WR)


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)

