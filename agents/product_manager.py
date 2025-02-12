from typing import Dict, Any
from utils.gemini_utils import GeminiWrapper
from workflows.workflow_state import WorkflowState

class ProductManagerAgent:
    def __init__(self):
        self.gemini = GeminiWrapper()
        
    async def create_user_story(self, state: WorkflowState) -> WorkflowState:
        """
        Convert requirements into a structured user story
        """
        print(f"Creating user story for requirements: {state.requirements}")
        prompt = f"""
        As a Product Manager, create a detailed user story from these requirements:
        {state.requirements}
        
        Format the response as:
        - Title
        - User Story (As a... I want... So that...)
        - Acceptance Criteria
        - Technical Notes
        """
        
        response = await self.gemini.generate_response(prompt)

        state.user_story = response
        state.status = "created"
        state.current_agent = "developer"
        print(f"state(product_manager): {state.current_agent}")
        return state

    

    async def validate_implementation(self, state: WorkflowState) -> WorkflowState:
        """
        Validate if the implementation meets requirements
        """
        prompt = f"""
        Review this implementation against the original user story:
        
        User Story:
        {state.user_story}
        
        Implementation:
        {state.code}
        
        Provide a detailed analysis of whether it meets requirements.
        End your analysis with either PASS or FAIL.
        """
        validation = await self.gemini.generate_response(prompt)
        state.validation_result = validation
        state.status = "completed"
        state.current_agent = "validate"
        print(f"validating pm")
        return state 