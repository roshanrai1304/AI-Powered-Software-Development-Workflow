from typing import Dict, Any
from utils.gemini_utils import GeminiWrapper
from workflows.workflow_state import WorkflowState
from agents.product_manager import ProductManagerAgent

class TesterAgent:
    def __init__(self):
        self.gemini = GeminiWrapper()
    
    async def test_implementation(self, state: WorkflowState) -> WorkflowState:
        """
        Test the implemented feature
        """
        prompt = f"""
        As a QA Tester, test this implementation:
        
        Code:
        {state.code}
        
        User Story:
        {state.user_story}
        
        Provide:
        1. Test cases
        2. Test results
        3. Bug reports if any
        4. Overall assessment
        
        End with either PASS or FAIL.
        """
        
        test_results = await self.gemini.generate_response(prompt)
        state.test_results = test_results
        state.status = "tested"
        state.current_agent = "validate"
        return state 
