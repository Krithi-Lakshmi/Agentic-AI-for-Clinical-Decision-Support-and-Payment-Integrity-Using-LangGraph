from langchain.text_splitter import CharacterTextSplitter

POLICIES = """
- Pre-authorization required for surgeries above $10,000
- Knee surgery requires documentation of failed physical therapy
- MRI requires physician referral
- Emergency claims bypass pre-authorization
"""

def retrieve_policy(query: str):
    # simple RAG simulation (you can replace with ChromaDB later)
    if "knee" in query.lower():
        return "Knee surgery requires documentation of failed physical therapy + pre-auth required"
    if "surgery" in query.lower():
        return "Pre-authorization required for surgeries above $10,000"
    return "General policy: claims must be medically necessary and pre-approved"
