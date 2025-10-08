import os, base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class KeyGenerator:
    def __init__(self):
        self.key_size = 2048 #minimum size

    def generate_key_pair(self):
        print(">>generating key...")
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,  # Do not change
            key_size=self.key_size,
        )
        self.public_key = self.private_key.public_key()
        print(">>succesfully generate")

    def generate_aes_key(self):
        self.key = os.urandom(32)

    def get_aes_key(self):
        encoded_key =  base64.b64encode(self.key)
        return encoded_key

    def get_private_key(self):
        return self.private_key
    
    def get_public_key(self):
        return self.public_key
    
    def get_key_pair(self):
        public_pem = self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PublicFormat.SubjectPublicKeyInfo)
        private_pem = self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                     encryption_algorithm=serialization.NoEncryption())
        return (public_pem, private_pem)