from colorama import Fore
from source import library
from ast import literal_eval
import tqdm
local_client_object = library.LocalClient()
local_client_object.ConnectToServer()

buffer_size = 100

class Command:
    def __init__(self, command, args) -> None:
        self.__command = command
        self.__args = args

    def __call__(self):
        return [self.__command, self.__args]

while True:
    command = input('command > ')
    if command != '':
        c = None
        if command.split(' ')[0] == 'open':
            c = Command('open', [command.split(' ')[1]])

            local_client_object.SendCommand(c)

            message_bits = literal_eval(local_client_object.GetServerCommandBits().decode())
            print(f'File founded (descriptor {message_bits[1][0].split('.')[-1]})')
            

            file = open(f'{message_bits[1][0]}', 'wb')
            saved_bytes = 0
            while True:
                library.synch(0.1)
                
                bytes_read = local_client_object.get_socket.recv(buffer_size)
                
                
                if bytes_read.decode() == 'finish': break
                file.write(bytes_read)
                saved_bytes+=len(bytes_read)
                print(f'Download: {Fore.YELLOW}{int(saved_bytes/message_bits[1][1]*100)}%{Fore.RESET}')
            

                
            print(f'Download [{Fore.GREEN}yes{Fore.RESET}]')
            file.close()
            print(f'File {file}saved ')
            

