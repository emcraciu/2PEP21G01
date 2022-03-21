import random
import threading
import socket
from threading import Thread


def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def primes(limit):
    result = []
    for i in range(1, limit + 1):
        if is_prime(i):
            result.append(i)
    return result


class AlreadySetError(Exception):
    pass


class Connector():
    __shared_secret = None
    __local_secret = None

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def generate_prime(self):
        primes_list = list(filter(lambda no: True if no > 129 else False, primes(256)))
        self.prime = primes_list[random.randint(0, len(primes_list) - 1)]
        self.prime = random.choice(primes_list)

    def get_prime(self, prime):
        if not getattr(self, "prime", False):
            self.prime = prime
        else:
            raise AlreadySetError('Value for prime already set to:', self.prime)

    def generate_base(self):
        if getattr(self, "prime", False):
            self.base = random.randint(2, self.prime - 1)
        else:
            raise AttributeError('Value for prime needs to be set first')

    def get_base(self, base):
        if not getattr(self, "base", False):
            self.base = base
        else:
            raise AlreadySetError('Value for base already set to:', self, base)

    def generate_local_secret(self):
        self.__local_secret = random.randint(2, self.prime)
        x = pow(self.base, self.__local_secret) % self.prime
        print(x)
        return x

    def get_secret(self, secret):
        self.__shared_secret = pow(secret, self.__local_secret) % self.prime + 129
        print(self.__shared_secret)


class Client(Connector):
    def start(self):
        self.sock.connect((self.host, self.port))
        self.generate_prime()
        self.sock.send(bytes(str(self.prime), encoding='UTF-8'))
        message = str(self.sock.recv(4096), encoding='UTF-8')
        print('Client ' + message)
        if message == 'okay':
            self.generate_base()
            self.sock.send(bytes(str(self.base), encoding='UTF-8'))
        message = str(self.sock.recv(4096), encoding='UTF-8')
        print('Client ' + message)
        if message == 'okay':
            self.generate_local_secret()


class Server(Connector):

    def __init__(self, host, port):
        super().__init__(host, port)
        self.sock.bind((self.host, self.port))

    def start(self):
        self.sock.listen(1)
        self.th1 = Thread(target=self.recv_msg)
        self.th1.start()

    def recv_msg(self):
        connection, addr = self.sock.accept()
        print(addr)
        with connection:
            message = str(connection.recv(4096), encoding='UTF-8')
            print('Server ' + message)
            self.prime = int(message)
            connection.send(bytes('okay', encoding='UTF-8'))
            message = str(connection.recv(4096), encoding='UTF-8')
            print('Server ' + message)
            self.base = int(message)
            connection.send(bytes('okay', encoding='UTF-8'))

    def stop(self):
        self.th1.join()


if __name__ == '__main__':
    client = Client('localhost', 1202)
    server = Server('localhost', 1202)
    server.start()
    client.start()
    server.stop()

    # client.generate_base()
    # server.get_base(client.base)
    # ss = server.generate_local_secret()
    # cs = client.generate_local_secret()
    # client.get_secret(ss)
    # server.get_secret(cs)
