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

    def dict(self, *args, **kwargs) -> dict:
        """Override dict method to ensure proper serialization"""
        return {
            "requirements": self.requirements,
            "user_story": self.user_story,
            "code": self.code,
            "context": self.context,
            "status": self.status,
            "current_agent": self.current_agent,
            "review_feedback": self.review_feedback,
            "test_results": self.test_results,
            "validation_result": self.validation_result
        }

    @classmethod
    def from_dict(cls, data: dict) -> "WorkflowState":
        """Create a WorkflowState instance from a dictionary"""
        return cls(**data)

    class Config:
        arbitrary_types_allowed = True 