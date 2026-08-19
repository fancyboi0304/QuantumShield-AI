import ast

from src.models.crypto_finding import CryptoFinding
from src.scanner.crypto_registry import CRYPTO_API_REGISTRY


def analyze_code(code: str, file_path: str) -> list[CryptoFinding]:
    tree = ast.parse(code)

    findings = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Attribute):
                continue

            if not isinstance(node.func.value, ast.Name):
                continue

            algorithm = node.func.value.id
            operation = node.func.attr

            api_key = (algorithm, operation)

            if api_key not in CRYPTO_API_REGISTRY:
                continue

            crypto_info = CRYPTO_API_REGISTRY[api_key]

            algorithm_name = crypto_info["algorithm"]

            key_size = None

            for keyword in node.keywords:
                if keyword.arg == "key_size":
                    if isinstance(keyword.value, ast.Constant):
                        key_size = keyword.value.value

            finding = CryptoFinding(
                algorithm=algorithm_name,
                operation=operation,
                key_size=key_size,
                file=file_path,
                line=node.lineno,
            )

            findings.append(finding)

    return findings


if __name__ == "__main__":
    file_path = "tests/sample_crypto.py"

    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    findings = analyze_code(code, file_path)

    for finding in findings:
        print(finding)