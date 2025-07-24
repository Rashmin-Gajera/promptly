class AgentState:
    def __init__(self, memory: dict):
        self.memory = memory


### app/core/coordinator.py
def central_coordinator(state):
    task = state.memory.get("task", "").lower()
    if "search" in task:
        return "SearchAgent"
    elif "code" in task:
        return "CodeGenAgent"
    elif "analyze" in task:
        return "DataAnalystAgent"
    elif "check" in task or "review" in task:
        return "CriticAgent"
    else:
        return "SearchAgent"