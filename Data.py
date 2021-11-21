# Data structures defined here.

from enum import Enum

class MessageType(Enum):
    GET = 1
    DELETE = 2
    UPDATE = 3

class Message:
    def __init__(self, messageType, payload):
        self.messageType = messageType
        self.payload = payload