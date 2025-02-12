from typing import Dict, Any
from utils.gemini_utils import GeminiWrapper
from workflows.workflow_state import WorkflowState

class ReviewerAgent:
    def __init__(self):
        self.gemini = GeminiWrapper()
    
    async def review_code(self, state: WorkflowState) -> WorkflowState:
        """
        Review the implemented code
        """
        prompt = f"""
        As a Code Reviewer, review this implementation:
        
        Code:
        {state.code}
        
        Consider:
        1. Code quality
        2. Best practices
        3. Potential bugs
        4. Performance issues
        
        End your review with either APPROVED or NEEDS_REVISION.
        """
        
        review = await self.gemini.generate_response(prompt)
        state.review_feedback = review
        state.status = "reviewed"
        state.current_agent = "tester"
        return state 