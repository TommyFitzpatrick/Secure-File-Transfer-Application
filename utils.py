# Password hashing using pycryptodome (SHA-512 + salt)

from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64
import hmac

def hash_password(password):
    salt = get_random_bytes(16)
    hasher = SHA512.new()
    hasher.update(salt + password.encode())
    hash_digest = hasher.digest()

    # Store salt and hash together, base64-encoded
    return base64.b64encode(salt + hash_digest).decode()


def verify_password(password, stored_b64):
    """Verify a plaintext `password` against a stored base64-encoded
    salt+sha512(salt+password) value produced by `hash_password`.

    Returns True when the password matches, False otherwise.
    """
    try:
        decoded = base64.b64decode(stored_b64)
    except Exception:
        return False

    if len(decoded) < 16:
        return False

    salt = decoded[:16]
    stored_digest = decoded[16:]

    hasher = SHA512.new()
    hasher.update(salt + password.encode())
    computed = hasher.digest()

    return hmac.compare_digest(computed, stored_digest)
