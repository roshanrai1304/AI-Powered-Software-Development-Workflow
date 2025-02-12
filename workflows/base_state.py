from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class BaseWorkflowState:
    """Base state class for the development workflow."""
    requirements: str
    context: Optional[Dict[str, Any]] = None
    status: Optional[str] = None
    review_feedback: Optional[str] = None
    validation_result: Optional[str] = None
    product_manager: Optional[str] = None
    developer: Optional[str] = None
    reviewer: Optional[str] = None
    tester: Optional[str] = None 