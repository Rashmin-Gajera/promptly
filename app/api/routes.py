from fastapi import APIRouter, HTTPException
from app.models.agent_models import AgentRequest, AgentResponse
from app.core.graph import build_agent_graph, AgentState

router = APIRouter()
graph = build_agent_graph()

@router.post("/run", response_model=AgentResponse)
async def run_agent(request: AgentRequest):
    try:
        state = AgentState(memory=request.dict())
        result = graph.invoke(state)
        return {"memory": result.memory}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
