def rag_agent(state):
    policy = retrieve_policy(state["claim"])
    return {"retrieved_policy": policy}


def risk_agent(state):
    if "pre-auth" in state["claim"].lower():
        return {"risk_score": "HIGH"}
    return {"risk_score": "LOW"}


def fraud_agent(state):
    if state["risk_score"] == "HIGH":
        return {"fraud_flag": "POTENTIAL ISSUE"}
    return {"fraud_flag": "CLEAR"}


def decision_agent(state):
    if state["risk_score"] == "HIGH":
        return {"decision": "SEND TO HUMAN REVIEW"}
    return {"decision": "APPROVE CLAIM"}
