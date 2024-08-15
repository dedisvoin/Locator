from source import library
import ast
import os
import tqdm

local_server_object = library.LocalServer('Pyls/')
local_server_object.InitServer()
local_server_object.StartWaitingConnects()

buffer_size = 100

def command_analize(command_data, user: library.User):
    if command_data[0] == 'open':
        file_name = command_data[1][0]
        file_size = os.path.getsize(local_server_object.get_path+file_name)
        print(file_name, file_size)

        user.get_socket.send(f'{['File founded!', [file_name, file_size] ]}'.encode())
        
        progress = tqdm.tqdm(range(file_size), f"Sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
        file = open(local_server_object.get_path + file_name, 'rb')
        library.synch(0)
        while True:
            library.synch(0.1)
            bytes_read = file.read(buffer_size)
            
            if not bytes_read: break

            user.get_socket.send(bytes_read)
            progress.update(len(bytes_read))
        
        user.get_socket.send('finish'.encode())

        

        

def commands_get():
    global local_server_object
    
    while True:
        library.synch()
        for user in local_server_object.get_users:
            try:
                bytes = local_server_object.WaitCommandBits(user)

                decoded_data = ast.literal_eval(bytes.decode())

                command_analize(decoded_data, user)
            except: ...
            
            
            
    

commands_get()