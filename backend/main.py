from fastapi import FastAPI
from routers import agent_router, health

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "D&D Assistant API is running."}

# Include routers
app.include_router(agent_router.router)
app.include_router(health.router)
