from fastapi import APIRouter
from ..agents.dnd_agent import DnDAgent

router = APIRouter()

@router.post("/agent/act")
def agent_act(input_data: dict):
    agent = DnDAgent(name="ExampleAgent")
    result = agent.act(input_data.get("input", ""))
    return {"result": result}
