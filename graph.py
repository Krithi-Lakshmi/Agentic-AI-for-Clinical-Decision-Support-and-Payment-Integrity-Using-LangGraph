from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from agents import rag_agent, risk_agent, fraud_agent, decision_agent
from state import ClaimState

workflow = StateGraph(ClaimState)

workflow.add_node("rag", rag_agent)
workflow.add_node("risk", risk_agent)
workflow.add_node("fraud", fraud_agent)
workflow.add_node("decision", decision_agent)

workflow.set_entry_point("rag")

workflow.add_edge("rag", "risk")
workflow.add_edge("risk", "fraud")
workflow.add_edge("fraud", "decision")
workflow.add_edge("decision", END)

checkpointer = MemorySaver()

app = workflow.compile(checkpointer=checkpointer)
