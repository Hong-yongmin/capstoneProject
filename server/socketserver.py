import socket
from keygenerator import KeyGenerator
from threading import Thread
# import ssl

class SocketServer:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080

    def start(self):
        print(">> starting server...")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.settimeout(1)
        self.server_socket.bind( (self.host, self.port) )
        self.server_socket.listen(1)
        print(">> server is waiting client")

        try:
            while True:
                try:
                    client_socket, client_addr = self.server_socket.accept()
                    print(">> client connected:", client_addr)
                    Thread(target=self.connect, args=(client_socket,), daemon=True).start()
                except socket.timeout:
                    continue
        except KeyboardInterrupt:
            self.server_socket.close()
            print(">> close server")

    def connect(self, client_socket):
        key_generator = KeyGenerator()
        key_generator.generate_key_pair()
        key_generator.generate_aes_key()
        public_key, private_key = key_generator.get_key_pair()
        aes_key = key_generator.get_aes_key()

        while True:
            data = client_socket.recv(1024)
            data_decode = data.decode("utf-8")
            if data_decode == "public" :
                client_socket.send(public_key)
                print(">>send public key")
            elif data_decode == "private" :
                client_socket.send(private_key)
                print(">>send private key")
            elif data_decode == "aes":
                client_socket.send(aes_key)
                print(">>send aes key")
            else :
                print(">>disconnected")
                client_socket.close()
                break

        
    