from dataclasses import dataclass


@dataclass
class CryptoFinding:
    algorithm: str
    operation: str
    key_size: int | None
    file: str
    line: int