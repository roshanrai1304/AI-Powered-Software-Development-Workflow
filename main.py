from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import workflow_routes
import uvicorn

app = FastAPI(
    title="LangGraph Development Workflow API",
    description="API for managing software development workflow using LangGraph",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(workflow_routes.router, prefix="/api/v1", tags=["workflow"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 