import socket
import time
from source.settings import LOCAL_IP, LOCAL_PORT

def synch(t: float = 0.01):
    time.sleep(t)

class Location:
    def __init__(self, port: int = LOCAL_PORT, host: str = LOCAL_IP) -> None:
        self.__port = port
        self.__host = host

    
    def get(self) -> list[str, int]:
        return [self.__host, self.__port]
    
LOCAL = Location(
    port = LOCAL_PORT, 
    host = LOCAL_IP
)

class ServerObject:
    def __init__(self) -> None:
        self.__socket = None
        self.__location = None


    @property
    def get_socket(self) -> socket.socket:
        return self.__socket
    
    @property
    def get_location(self) -> Location:
        return self.__location
    
    def Init(self, location: Location = LOCAL):
        self.__location = location
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        l = (self.__location.get()[0], self.__location.get()[1])
        self.__socket.bind(l)
        self.__socket.listen()
        
    def WaitConn(self) -> list:
        client, client_addr = self.__socket.accept()
        client.setblocking(0)
        return [client, client_addr]

class ClientObject:
    def __init__(self) -> None:
        self.__socket = None
        self.__location = None

    @property
    def get_socket(self) -> socket.socket:
        return self.__socket
    
    @property
    def get_location(self) -> Location:
        return self.__location
    
    def Connect(self, location: Location = LOCAL):
        self.__location = location
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((self.__location.get()[0], self.__location.get()[1]))

    def GetServerCommandBits(self):
        return self.__socket.recv(2024)


class User:
    def __init__(self, location: Location | None = None, socket: socket.socket = None) -> None:
        self.__location = location
        self.__socket = socket

    @property
    def get_socket(self) -> socket.socket:
        return self.__socket
    
    @property
    def get_location(self) -> Location:
        return self.__location
    

