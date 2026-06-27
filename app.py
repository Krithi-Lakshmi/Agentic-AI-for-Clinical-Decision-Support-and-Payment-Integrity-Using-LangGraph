import streamlit as st
from graph import app

st.title("🏥 Agentic Claims Intelligence System")

claim = st.text_area("Enter Claim")

if st.button("Analyze"):
    config = {"configurable": {"thread_id": "claim-001"}}

    result = app.invoke({"claim": claim}, config=config)

    st.subheader("📚 Policy Context")
    st.write(result["policy_context"])

    st.subheader("⚠️ Risk Score")
    st.write(result["risk_score"])

    st.subheader("🧠 Decision")
    st.write(result["decision"])

    st.subheader("📄 Explanation (IMPORTANT)")
    st.text(result["explanation"])
