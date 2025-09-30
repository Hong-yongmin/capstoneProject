from socket import *
# import ssl

class SocketServer:
    def __init__(self, key_pair):
        self.host = "127.0.0.1"
        self.port = 8080
        self.public_key, self.private_key = key_pair

    def start(self):
        print(">>starting server...")
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind( (self.host, self.port) )
        self.server_socket.listen(1)
        print(">>server is waiting client")

        self.connect()

    def connect(self):
        #self.server_socket.settimeout(5)  # 5초 대기 후 socket.timeout 예외 발생
        self.connection_socket, self.addr = self.server_socket.accept()
        print(">>client is connected")

        while True:
            data = self.connection_socket.recv(1024)
            data_decode = data.decode("utf-8")
            if data_decode == "public" :
                self.connection_socket.send(self.public_key)
                print(">>send public key")
            elif data_decode == "private" :
                self.connection_socket.send(self.private_key)
                print(">>send private key")
            else :
                print(">>disconnected")
                break

        self.server_socket.close()
        print(">>close server")
    