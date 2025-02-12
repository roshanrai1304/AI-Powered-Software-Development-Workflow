from typing import Dict, Any
from utils.gemini_utils import GeminiWrapper
from models.workflow_state import WorkflowState
from langgraph.graph import Graph, StateGraph
from pydantic import BaseModel

class DeveloperAgent:
    def __init__(self):
        self.gemini = GeminiWrapper()
    
    async def implement_feature(self, state: WorkflowState) -> WorkflowState:
        """
        Generate implementation code based on the user story
        """
        prompt = f"""
        As a Developer, create a Python implementation for this user story:
        {state.user_story}
        
        Provide:
        1. Implementation code
        2. Unit tests
        3. Documentation
        """
        implementation = await self.gemini.generate_response(prompt)
        state.code = implementation
        state.status = "implemented"
        state.current_agent = "reviewer"
        return state



    
    async def fix_issues(self, state: WorkflowState) -> WorkflowState:
        """
        Fix issues based on review feedback
        """
        prompt = f"""
        Fix the following issues in the code:
        
        Original Code:
        {state.code}
        
        Review Feedback:
        {state.review_feedback}
        """
        print(f"Fixing issues:")
        updated_code = await self.gemini.generate_response(prompt)
        state.code = updated_code
        state.status = "fixed"
        state.current_agent = "validate"
        return state 