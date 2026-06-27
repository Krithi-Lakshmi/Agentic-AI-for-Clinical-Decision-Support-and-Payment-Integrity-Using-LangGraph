from rag.retriever import retrieve_policy

def rag_node(state):
    policy = retrieve_policy(state["claim"])
    return {
        "policy_context": policy
    }

def risk_node(state):
    claim = state["claim"].lower()

    score = 0

    if "pre-authorization" in claim:
        score += 0.7

    if "surgery" in claim:
        score += 0.3

    return {
        "risk_score": min(score, 1.0)
    }

def decision_node(state):

    risk = state["risk_score"]
    policy = state["policy_context"]

    if risk > 0.6:

        decision = "FLAG FOR REVIEW"

        explanation = f"""
Decision triggered due to high risk score ({risk}).

Relevant Policy:
{policy}

Reason:
Claim matches high-cost / missing authorization patterns.
"""

    else:

        decision = "APPROVE CLAIM"

        explanation = f"""
Low risk claim.

Relevant Policy:
{policy}

No policy violations detected.
"""

    return {
        "decision": decision,
        "explanation": explanation
    }
