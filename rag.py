from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

POLICIES = [
    "Pre-authorization required for surgeries above $10,000",
    "Knee surgery requires failed physical therapy documentation",
    "Emergency claims bypass pre-authorization",
    "MRI requires physician referral"
]

def build_vectorstore():
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(POLICIES, embeddings)


vectorstore = build_vectorstore()

def retrieve_policy(query: str):
    docs = vectorstore.similarity_search(query, k=2)
    return " | ".join([d.page_content for d in docs])
