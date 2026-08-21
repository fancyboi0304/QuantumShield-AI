from dataclasses import dataclass


@dataclass
class RiskAssessment:
    algorithm: str
    category: str
    risk_level: str
    quantum_vulnerable: bool
    reason: str
    recommendation: str