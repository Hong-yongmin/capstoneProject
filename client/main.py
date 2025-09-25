from socketclient import SocketClient
from encryption import Encryption

def main():
    client = SocketClient()
    client.start()
    key = client.get_key(0)
    print(key)
    client.stop()

if __name__ == '__main__':
    main()