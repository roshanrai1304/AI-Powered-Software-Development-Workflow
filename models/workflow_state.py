from typing import Dict, Any, Optional
from pydantic import BaseModel


class WorkflowState(BaseModel):
    requirements: str
    user_story: Optional[str] = None
    code: Optional[str] = None
    review_feedback: Optional[str] = None
    test_results: Optional[str] = None
    validation_result: Optional[str] = None
    status: Optional[str] = None
    current_agent: Optional[str] = None
    context: Optional[Dict[str, Any]] = None
    product_manager: Optional[str] = None
    developer: Optional[str] = None
    reviewer: Optional[str] = None
    tester: Optional[str] = None

