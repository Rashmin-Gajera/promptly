def critic_agent(state):
    code = state.memory.get("code_output", "")
    decision = "approve" if "error" not in code else "revise"
    state.memory["decision"] = decision
    return state