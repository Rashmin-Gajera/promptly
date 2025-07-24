# Yukti - Smart Health Assistant

A modular, large-scale agentic AI platform using FastAPI, LangChain, and LangGraph.

## Features
- Hub-and-spoke agent coordination
- Flexible routing logic
- Pluggable agents
- REST API interface via FastAPI

## Folder Structure

Promptly/  
├── app/
│   ├── main.py                  # FastAPI entrypoint  
│   ├── api/                     # API route handlers  
│   │   └── routes.py  
│   ├── core/                    # Core logic & LangGraph builder  
│   │   ├── graph.py             # Graph definition  
│   │   ├── coordinator.py       # Central coordinator logic  
│   │   └── state.py             # AgentState definition  
│   ├── agents/                  # All specialized agents  
│   │   ├── base.py              # BaseAgent interface  
│   │   ├── search_agent.py  
│   │   ├── codegen_agent.py  
│   │   └── critic_agent.py  
│   ├── tools/                   # LangChain tools  
│   │   └── web_search.py  
│   ├── memory/                  # Memory modules (e.g., ChromaDB)  
│   │   └── vectorstore.py  
│   └── models/                  # Request/response schemas  
│       └── agent_models.py  
├── requirements.txt  
└── README.md  


## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs to test the API.