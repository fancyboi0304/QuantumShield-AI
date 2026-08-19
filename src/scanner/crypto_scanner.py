from pathlib import Path

from src.scanner.ast_analyzer import analyze_code


CRYPTO_PATTERNS = {
    "RSA": ["RSA", "rsa"],
    "ECC": ["ECC", "elliptic curve"],
    "ECDSA": ["ECDSA", "ecdsa"],
    "ECDH": ["ECDH", "ecdh"],
    "AES": ["AES", "aes"],
    "SHA-256": ["SHA-256", "sha256", "SHA256", "sha_256"],
    "SHA-512": ["SHA-512", "sha512", "SHA512", "sha_512"],
}


def scan_text(text: str) -> list[str]:
    """Scan text and return detected cryptographic technologies."""

    findings = []

    for algorithm, patterns in CRYPTO_PATTERNS.items():
        for pattern in patterns:
            if pattern in text:
                findings.append(algorithm)
                break

    return findings


def scan_file(file_path: str) -> list[str]:
    """Read a file and scan it for cryptographic technologies."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    text = path.read_text(encoding="utf-8")

    return scan_text(text)


def scan_file_ast(file_path: str):
    """Read a Python file and analyze it using AST."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    text = path.read_text(encoding="utf-8")

    return analyze_code(text, file_path)


def main():
    target_file = input("Enter file path to scan: ")

    try:
        keyword_results = scan_file(target_file)

        if target_file.endswith(".py"):
            ast_results = scan_file_ast(target_file)
        else:
            ast_results = []

        print()
        print("=== QuantumShield AI Crypto Scanner ===")
        print()

        if keyword_results:
            print("Keyword-based detection:")

            for result in keyword_results:
                print(f"- {result}")
        else:
            print("No keyword-based detections.")

        print()

        if ast_results:
            print("AST-based findings:")

            for finding in ast_results:
                print(f"- Algorithm: {finding.algorithm}")
                print(f"  Operation: {finding.operation}")
                print(f"  Key Size: {finding.key_size}")
                print(f"  File: {finding.file}")
                print(f"  Line: {finding.line}")
                print()
        else:
            print("No AST-based crypto findings.")

    except FileNotFoundError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()