from typing import TypedDict, List

class ClaimState(TypedDict):
    claim: str
    retrieved_policy: str
    risk_score: str
    fraud_flag: str
    decision: str
