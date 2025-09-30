from socketclient import SocketClient
from filebrowser import FileBrowser

def main():
    client = SocketClient()
    client.start()
    key = client.get_key(0) # public key 가져옴
    client.stop()
    print(key)
    file_browser = FileBrowser(key)
    file_browser.browse('./../target/*', 0)

if __name__ == '__main__':
    main()