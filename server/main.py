from socketserver import SocketServer
from keygenerator import KeyGenerator

def main():
    key_generator = KeyGenerator()
    key_generator.generate_key_pair()
    
    server = SocketServer(key_generator.get_key_pair())
    server.start()

if __name__ == '__main__':
    main()