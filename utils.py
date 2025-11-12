# Password hashing using pycryptodome (SHA-512 + salt)

from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64

def hash_password(password):
    salt = get_random_bytes(16)
    hasher = SHA512.new()
    hasher.update(salt + password.encode())
    hash_digest = hasher.digest()

    # Store salt and hash together, base64-encoded
    return base64.b64encode(salt + hash_digest).decode()
