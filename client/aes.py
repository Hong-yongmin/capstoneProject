import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

class AES:
    def __init__(self, key, iv):
        self.key = key
        self.cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

    def encrypt(self, message):
        padder = padding.PKCS7(128).padder()
        padded_message =  padder.update(message) + padder.finalize()
        encryptor = self.cipher.encryptor()
        return encryptor.update(padded_message) + encryptor.finalize()
    
    def decrypt(self, message):
        decryptor = self.cipher.decryptor()
        decrypted_message = decryptor.update(message) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(decrypted_message) + unpadder.finalize()