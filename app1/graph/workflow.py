from langgraph.graph import StateGraph, START, END

from app.graph.state import TrackState
from app.graph.checkpointer import get_checkpointer
from app.graph.nodes import GraphNodes


def build_workflow(checkpointer=None):

    nodes = GraphNodes()

    graph = StateGraph(TrackState)

    # -------------------
    # Nodes
    # -------------------
    graph.add_node("refine_question", nodes.refine_question)
    graph.add_node("final_answer", nodes.final_answer)
    graph.add_node("update_history", nodes.update_history)

    # -------------------
    # Edges
    # -------------------
    graph.add_edge(START, "refine_question")
    graph.add_edge("refine_question", "final_answer")
    graph.add_edge("final_answer", "update_history")
    graph.add_edge("update_history", END)

    # -------------------
    # Compile with safe checkpointer
    # -------------------
    if checkpointer is None:
        checkpointer = get_checkpointer()

    workflow = graph.compile(checkpointer=checkpointer)

    return workflow

def get_workflow():
    checkpointer = get_checkpointer()
    return build_workflow(checkpointer=checkpointer)