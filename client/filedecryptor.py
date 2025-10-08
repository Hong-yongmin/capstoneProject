import glob
import os
from aes import AES
from filechecker import FileChecker

class FileDecryptor:
    def __init__(self, key, iv):
        self.decryptor = AES(key, iv)
        self.file_checker = FileChecker()

    def decrypt(self, target):
        file_list = glob.glob(target)

        for file in file_list:
            if os.path.isdir(file):
                self.decrypt(file+'/*')
            
            else:
                if not self.file_checker.check_encrypted_file(file):
                    continue

                with open(file, 'rb') as f:
                    decrypted_file = self.decryptor.decrypt(f.read())

                with open(file, 'wb') as f:
                    f.write(decrypted_file)
            
                new_name = file[0:-10] # .encrypted 제거
                os.rename(file, new_name)