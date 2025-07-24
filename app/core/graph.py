from langgraph.graph import StateGraph, END
from app.core.state import AgentState
from app.core.coordinator import central_coordinator
from app.agents.search_agent import search_agent
from app.agents.codegen_agent import codegen_agent
from app.agents.critic_agent import critic_agent

# Optional new agents
try:
    from app.agents.data_analyst_agent import data_analyst_agent
except ImportError:
    data_analyst_agent = None

def build_agent_graph():
    graph = StateGraph(AgentState)

    graph.add_node("SearchAgent", search_agent)
    graph.add_node("CodeGenAgent", codegen_agent)
    graph.add_node("CriticAgent", critic_agent)
    if data_analyst_agent:
        graph.add_node("DataAnalystAgent", data_analyst_agent)

    graph.add_node("CentralCoordinator", lambda s: s)
    graph.set_entry_point("CentralCoordinator")

    graph.add_conditional_edges("CentralCoordinator", central_coordinator)

    graph.add_edge("SearchAgent", "CentralCoordinator")
    graph.add_edge("CodeGenAgent", "CriticAgent")
    graph.add_edge("CriticAgent", END)
    if data_analyst_agent:
        graph.add_edge("DataAnalystAgent", END)

    return graph.compile()

