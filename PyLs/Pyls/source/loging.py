import time

def get_time():
    h = time.gmtime(time.time()).tm_hour
    m = time.gmtime(time.time()).tm_min
    s = time.gmtime(time.time()).tm_sec
    return f'({h}:{m}:{s})'

class Logger:
    def __init__(self, file: str = 'logs.txt') -> None:
        self.__file_path = file

        self.__logs = []

        self.__file_object = open(self.__file_path, 'w')
        self.__file_object.close()

    def update_log(self):
        for log in self.__logs:
            self.__file_object.write(log + '\n')

    def log_server_created_succes(self, location, path):
        self.__file_object = open(self.__file_path, 'w+')
        self.__logs.append(
            f'{get_time()} - Host started {location=} {path=} [ yes ]'
        )
        print(f'{get_time()} - Host started {location=} {path=} [ yes ]')
        self.update_log()
        self.__file_object.close()
    
    def log_server_created_fail(self, location, path):
        self.__file_object = open(self.__file_path, 'w+')
        self.__logs.append(
            f'{get_time()} - Host not started {location=} {path=} [ no ]'
        )
        print(f'{get_time()} - Host not started {location=} {path=} [ no ]')
        self.update_log()
        self.__file_object.close()

    def log_start_waiting_connect(self):
        self.__file_object = open(self.__file_path, 'w+')
        self.__logs.append(
            f'{get_time()} - Host start waited connects...'
        )
        print(f'{get_time()} - Host start waited connects...')
        self.update_log()
        self.__file_object.close()

    def log_client_connected(self, port, host):
        self.__file_object = open(self.__file_path, 'w+')
        self.__logs.append(
            f'{get_time()} - Client connected {port=} {host=}'
        )
        print(f'{get_time()} - Client connected {port=} {host=}')
        self.update_log()
        self.__file_object.close()

    def log_client_connect_succes(self, port, host):
        self.__file_object = open(self.__file_path, 'w+')
        self.__logs.append(
            f'{get_time()} - Connected to host {port=} {host=}'
        )
        print(f'{get_time()} - Connected to host {port=} {host=}')
        self.update_log()
        self.__file_object.close()