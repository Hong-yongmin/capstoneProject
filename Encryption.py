from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generate_key_pair():
    key_size = 2048  # Should be at least 2048

    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Do not change
        key_size=key_size,
    )

    public_key = private_key.public_key()
    return private_key, public_key

def encrypt(message, public_key):
    return public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

message = b"Hello World!"

private_key, public_key = generate_key_pair()

message_encrypted = encrypt(message, public_key)

print(f"Encrypted Text: {message_encrypted.hex()}")

def decrypt(message_encrypted, private_key):
    try:
        message_decrypted = private_key.decrypt(
            message_encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return f"Decrypted Message: {message_decrypted}"
    except ValueError:
        return "Failed to Decrypt"
    
message_decrypted = decrypt(message_encrypted, private_key)
print(message_decrypted)