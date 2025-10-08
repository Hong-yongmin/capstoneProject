from socket import *
from keygenerator import KeyGenerator
from threading import Thread
# import ssl

class SocketServer:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080

    def start(self):
        print(">>starting server...")
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind( (self.host, self.port) )
        self.server_socket.listen(1)
        print(">>server is waiting client")

        self.connection_socket, self.addr = self.server_socket.accept()
        print(">>client is connected")
        Thread(target = self.connect()).start()

    def connect(self):
        #self.server_socket.settimeout(5)  # 5초 대기 후 socket.timeout 예외 발생
        key_generator = KeyGenerator()
        key_generator.generate_key_pair()
        key_generator.generate_aes_key()
        public_key, private_key = key_generator.get_key_pair()
        aes_key = key_generator.get_aes_key()

        while True:
            data = self.connection_socket.recv(1024)
            data_decode = data.decode("utf-8")
            if data_decode == "public" :
                self.connection_socket.send(public_key)
                print(">>send public key")
            elif data_decode == "private" :
                self.connection_socket.send(private_key)
                print(">>send private key")
            elif data_decode == "aes":
                self.connection_socket.send(aes_key)
                print(">>send aes key")
            else :
                print(">>disconnected")
                break

        self.server_socket.close()
        print(">>close server")
    