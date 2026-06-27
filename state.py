from typing import TypedDict

class ClaimState(TypedDict):
    claim: str
    policy_context: str
    risk_score: float
    decision: str
    explanation: str
