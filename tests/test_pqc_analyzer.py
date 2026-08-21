from src.models.crypto_finding import CryptoFinding
from src.pqc.pqc_analyzer import analyze_finding


test_findings = [
    CryptoFinding(
        algorithm="RSA",
        operation="generate_private_key",
        key_size=2048,
        file="sample.py",
        line=1,
    ),
    CryptoFinding(
        algorithm="SHA-256",
        operation="SHA256",
        key_size=None,
        file="sample.py",
        line=10,
    ),
]


for finding in test_findings:
    assessment = analyze_finding(finding)

    assessment = analyze_finding(finding)

    print()
    print("=" * 50)
    print(assessment)