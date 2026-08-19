from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

digest = hashes.SHA256()