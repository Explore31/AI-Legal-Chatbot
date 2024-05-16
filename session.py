from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_session_key():
    # Generate a random 32-byte (256-bit) key
    key = hashes.Hash(hashes.SHA256(), backend=default_backend())
    key.update(b"your_secret_seed")  # Add a secret seed for additional randomness
    session_key = key.finalize()
    return session_key

# Example usage
session_key = generate_session_key()
print("Session Key:", session_key.hex())
