import socket
from threading import Thread

message = """" message """


def write_to_file1(message: str):
    with open('my_file', 'a') as file:
        file.write(f'Writer1: {message}')


def write_to_file2(message: str):
    with open('my_file', 'a') as file:
        file.write(f'Writer2: {message}')


for i in range(100):
    th1 = Thread(target=write_to_file1, args=('message1' * 10000,))
    th1.start()
# th2 = Thread(target=write_to_file2, args=('message2',))

# th1.start()
# th2.start()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(type(sock))
sock.
