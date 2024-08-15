from source.engine import LOCAL, Location
from source.engine import ServerObject, ClientObject, User
from source.engine import synch
from source.loging import Logger

from threading import Thread

class LocalServer(ServerObject):
    def __init__(self, path: str | None = None, logs_path: str = 'host_logs.txt') -> None:
        super().__init__()
        self.__path = path
        self.__users = []
        self.__logger = Logger(logs_path)

    @property
    def get_path(self) -> str:
        return self.__path

    @property
    def get_users(self) -> list[User]:
        return self.__users

    def InitServer(self, location: Location = LOCAL):
        try:
            super().Init(location)
            self.__logger.log_server_created_succes(self.get_location.get(), self.__path)
        except:
            self.__logger.log_server_created_fail(self.get_location.get(), self.__path)
            
    
    def Wait(self):
        self.__logger.log_start_waiting_connect()
        
        while True:
            
            client, ip = self.WaitConn()
            self.__users.append(User(Location(ip[1], ip[0]), client))
            self.__logger.log_client_connected(ip[1], ip[0])
    
    def StartWaitingConnects(self):
        thread = Thread(target = self.Wait, daemon=False)
        thread.start()

    def WaitCommandBits(self, user: User):
        return user.get_socket.recv(1024)

class LocalClient(ClientObject):
    def __init__(self, logs_path: str = 'client_logs.txt') -> None:
        super().__init__()
        self.__logger = Logger(logs_path)

    def ConnectToServer(self, location: Location = LOCAL):
        self.Connect(location)
        self.__logger.log_client_connect_succes(self.get_location.get()[1], self.get_location.get()[0])

    def SendCommand(self, command):
        name = command()[0]
        args = command()[1]
        self.get_socket.send(f'{[name, args]}'.encode())
