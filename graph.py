from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from state import ClaimState
from graph_nodes import rag_node, risk_node, decision_node

workflow = StateGraph(ClaimState)

workflow.add_node("rag", rag_node)
workflow.add_node("risk", risk_node)
workflow.add_node("decision", decision_node)

workflow.set_entry_point("rag")

workflow.add_edge("rag", "risk")
workflow.add_edge("risk", "decision")
workflow.add_edge("decision", END)

checkpointer = MemorySaver()

app = workflow.compile(checkpointer=checkpointer)
