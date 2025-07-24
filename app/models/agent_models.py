from pydantic import BaseModel
from typing import Optional, Dict

class AgentRequest(BaseModel):
    task: str
    query: Optional[str] = None
    data_task: Optional[str] = None

class AgentResponse(BaseModel):
    memory: Dict[str, str]
