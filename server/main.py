from socketserver import SocketServer
from keygenerator import KeyGenerator

def main():
    server = SocketServer()
    server.start()

if __name__ == '__main__':
    main()