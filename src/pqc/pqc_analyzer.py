from src.models.crypto_finding import CryptoFinding
from src.models.risk_assessment import RiskAssessment


RISK_RULES = {
    "RSA": {
        "category": "Public-Key Cryptography",
        "risk_level": "HIGH",
        "quantum_vulnerable": True,
        "reason": (
            "RSA is vulnerable to Shor's algorithm, which can "
            "efficiently factor large integers on a quantum computer."
        ),
        "recommendation": (
            "Migrate to a NIST-standardized post-quantum "
            "cryptographic algorithm."
        ),
    },
    "ECDSA": {
        "category": "Digital Signature",
        "risk_level": "HIGH",
        "quantum_vulnerable": True,
        "reason": (
            "ECDSA relies on the elliptic curve discrete logarithm "
            "problem, which is vulnerable to Shor's algorithm."
        ),
        "recommendation": (
            "Consider post-quantum digital signature schemes."
        ),
    },
    "ECDH": {
        "category": "Key Exchange",
        "risk_level": "HIGH",
        "quantum_vulnerable": True,
        "reason": (
            "ECDH relies on elliptic curve discrete logarithms and "
            "is vulnerable to Shor's algorithm."
        ),
        "recommendation": (
            "Consider post-quantum key exchange mechanisms."
        ),
    },
    "AES": {
        "category": "Symmetric Encryption",
        "risk_level": "MEDIUM",
        "quantum_vulnerable": False,
        "reason": (
            "Grover's algorithm reduces the effective security "
            "strength of symmetric cryptography."
        ),
        "recommendation": (
            "Use sufficiently large key sizes such as AES-256."
        ),
    },
    "SHA-256": {
        "category": "Hash Function",
        "risk_level": "MEDIUM",
        "quantum_vulnerable": False,
        "reason": (
            "Grover's algorithm can accelerate brute-force "
            "searches against hash functions."
        ),
        "recommendation": (
            "Consider stronger hash functions where appropriate."
        ),
    },
    "SHA-512": {
        "category": "Hash Function",
        "risk_level": "LOW",
        "quantum_vulnerable": False,
        "reason": (
            "SHA-512 retains a strong security margin even under "
            "Grover's algorithm."
        ),
        "recommendation": (
            "Continue using SHA-512 where suitable."
        ),
    },
}


def analyze_finding(finding: CryptoFinding) -> RiskAssessment:
    rule = RISK_RULES.get(finding.algorithm)

    if rule:
        return RiskAssessment(
            algorithm=finding.algorithm,
            category=rule["category"],
            risk_level=rule["risk_level"],
            quantum_vulnerable=rule["quantum_vulnerable"],
            reason=rule["reason"],
            recommendation=rule["recommendation"],
        )

    return RiskAssessment(
        algorithm=finding.algorithm,
        category="Unknown",
        risk_level="UNKNOWN",
        quantum_vulnerable=False,
        reason="No quantum risk rule is defined.",
        recommendation="Manual review required.",
    )