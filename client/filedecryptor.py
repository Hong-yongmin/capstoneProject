import glob
import os
from decryption import Decryption

class FileDecryptor:
    def __init__(self, private_key):
        self.decryptor = Decryption(private_key)

    def decrypt(self, target):
        file_list = glob.glob(target)

        for file in file_list:
            with open(file, 'rb') as f:
                decrypted_file = self.decryptor.decrypt(f.read())

            with open(file, 'wb') as f:
                f.write(decrypted_file)
            
            new_name = file[0:-10] # .encrypted 제거
            os.rename(file, new_name)