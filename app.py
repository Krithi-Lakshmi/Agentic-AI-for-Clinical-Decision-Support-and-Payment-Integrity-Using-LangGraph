import streamlit as st
from graph import app

st.title("🧠 Agentic AI Clinical Claims Review System")

claim_input = st.text_area("Enter Claim Details")

if st.button("Run Analysis"):
    config = {"configurable": {"thread_id": "claim-001"}}

    result = app.invoke({"claim": claim_input}, config=config)

    st.subheader("📚 Retrieved Policy")
    st.write(result["retrieved_policy"])

    st.subheader("⚠️ Risk Score")
    st.write(result["risk_score"])

    st.subheader("🚨 Fraud Flag")
    st.write(result["fraud_flag"])

    st.subheader("🧾 Final Decision")
    st.write(result["decision"])
