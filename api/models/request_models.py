from pydantic import BaseModel, Field, constr
from typing import Optional, Dict, Any, List, Union

class TechStackContext(BaseModel):
    project_type: str = Field(..., description="Type of the project (backend, frontend, full-stack)")
    tech_stack: List[str] = Field(default_factory=list, description="List of technologies to be used")
    priority: str = Field(..., description="Project priority (high, medium, low)")
    security_requirements: Optional[List[str]] = Field(default_factory=list)
    performance_requirements: Optional[Dict[str, Union[str, int]]] = None
    deployment: Optional[str] = None
    monitoring: Optional[str] = None

class RequirementsRequest(BaseModel):
    requirements: str = Field(
        ...,
        description="Detailed project requirements",
        example="Create a REST API for user management with CRUD operations"
    )
    context: Optional[TechStackContext] = Field(
        default=None,
        description="Additional context for the project"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "requirements": """
                Create a Todo List API with:
                1. CRUD operations for tasks
                2. Task prioritization
                3. Due dates
                4. Categories/tags
                """,
                "context": {
                    "project_type": "backend",
                    "tech_stack": ["FastAPI", "PostgreSQL", "JWT"],
                    "priority": "high",
                    "security_requirements": ["HTTPS", "JWT"],
                    "performance_requirements": {
                        "max_response_time": "200ms",
                        "concurrent_users": 100
                    }
                }
            }
        }

class WorkflowStage(BaseModel):
    name: str = Field(..., description="Name of the workflow stage")
    status: str = Field(..., description="Status of the stage")
    output: Optional[Dict[str, Any]] = Field(default=None, description="Stage output")

class WorkflowResponse(BaseModel):
    status: str = Field(..., description="Overall workflow status")
    message: str = Field(..., description="Status message")
    data: Dict[str, Any] = Field(
        ...,
        description="Workflow execution data including all stages"
    )
    stages: Optional[List[WorkflowStage]] = Field(
        default_factory=list,
        description="Detailed information about each workflow stage"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Workflow completed successfully",
                "data": {
                    "user_story": "...",
                    "code": "...",
                    "review_feedback": "...",
                    "test_results": "...",
                    "validation_result": "..."
                },
                "stages": [
                    {
                        "name": "product_manager",
                        "status": "completed",
                        "output": {"user_story": "..."}
                    },
                    {
                        "name": "developer",
                        "status": "completed",
                        "output": {"code": "..."}
                    }
                ]
            }
        } 