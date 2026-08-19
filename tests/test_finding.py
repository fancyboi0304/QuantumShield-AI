from src.models.crypto_finding import CryptoFinding


finding = CryptoFinding(
    algorithm="RSA",
    operation="generate_private_key",
    key_size=2048,
    file="tests/sample_crypto.py",
    line=2,
)


print(finding)