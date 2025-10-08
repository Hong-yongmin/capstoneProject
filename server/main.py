from socketserver import SocketServer
from keygenerator import KeyGenerator

def main():
    key_generator = KeyGenerator()
    key_generator.generate_key_pair()
    key_generator.generate_aes_key()
    
    server = SocketServer(key_generator.get_key_pair(), key_generator.get_aes_key())
    server.start()

if __name__ == '__main__':
    main()