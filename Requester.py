#Implement Client requester code here. The following is example code from https://pymotw.com/2/socket/tcp.html
import socket
import sys
from Data import MessageType
from Data import Message

#Testing data
#print >>sys.stderr, 'Enum "%s"' % MessageType(2)
#message = Message(MessageType(2), "Test string")
#print >>sys.stderr, 'Message "%s"' % message.messageType
#print >>sys.stderr, 'Message "%s"' % message.payload

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    #Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    #look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'recieved "%s"' % data
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
