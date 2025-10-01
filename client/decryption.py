from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class Decryption:
    def __init__(self, private_key):
        self.private_key = private_key

    def decrypt(self, message_encrypted):
        try:
            message_decrypted = self.private_key.decrypt(
                message_encrypted,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return message_decrypted
        except ValueError:
            return "Failed to Decrypt"