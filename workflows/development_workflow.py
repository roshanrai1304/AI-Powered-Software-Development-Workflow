from typing import Dict, Any, TypeVar, Annotated, Optional, Union, Literal, Type
from langgraph.graph import Graph, StateGraph
from agents.product_manager import ProductManagerAgent
from agents.developer import DeveloperAgent
from agents.reviewer import ReviewerAgent
from agents.tester import TesterAgent
from .workflow_state import WorkflowState
from pydantic import BaseModel

# Define a schema class for the state
class WorkflowStateDict(BaseModel):
    requirements: str
    user_story: Optional[str] = None
    code: Optional[str] = None
    review_feedback: Optional[str] = None
    test_results: Optional[str] = None
    validation_result: Optional[str] = None
    status: Optional[str] = None
    current_agent: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

def create_workflow() -> Graph:
    # Initialize agents
    pm_agent = ProductManagerAgent()
    dev_agent = DeveloperAgent()
    review_agent = ReviewerAgent()
    test_agent = TesterAgent()
    
    # Define routing functions first
    def after_review(state: Dict) -> Literal["fix_issues", "tester"]:
        if not state.get("review_feedback"):
            return "fix_issues"
        return "tester" if "APPROVED" in state["review_feedback"] else "fix_issues"
    
    def after_validate(state: Dict) -> Literal["developer", "done"]:
        print(f"state(validate): after validate")
        if state.get("status") == "completed":
            return "done"  # Keep the self-loop but don't modify state
        return "developer" if state.get("validation_result") == "PASS" else "done"


    

    # Create workflow with WorkflowStateDict
    workflow = StateGraph(WorkflowStateDict)
    
    # Define nodes with agent methods that return Dict
    async def product_manager_node(state: Dict) -> Dict:
        workflow_state = WorkflowState(**state.dict())
        result = await pm_agent.create_user_story(workflow_state)   
        print(f"state(product_manager): {state.current_agent}")
        return result.dict()

    async def developer_node(state: Dict) -> Dict:
        workflow_state = WorkflowState(**state.dict())
        result = await dev_agent.implement_feature(workflow_state)
        print(f"state(developer): {state.current_agent}")
        return result.dict()

    async def reviewer_node(state: Dict) -> Dict:
        workflow_state = WorkflowState(**state.dict())
        result = await review_agent.review_code(workflow_state)
        print(f"state(reviewer): {state.current_agent}")
        return result.dict()


    async def tester_node(state: Dict) -> Dict:
        print(f"tester is there")
        workflow_state = WorkflowState(**state.dict())
        result = await test_agent.test_implementation(workflow_state)
        print(f"state(tester): {state.current_agent}")
        return result.dict()

    async def fix_issues_node(state: Dict) -> Dict:
        workflow_state = WorkflowState(**state.dict())
        result = await dev_agent.fix_issues(workflow_state)
        print(f"state(fix_issues): {state.current_agent}")
        return result.dict()

    async def validate_node(state: Dict) -> Dict:
        # If already completed, just return the state without modifications
        print(f"state(validate): {state.current_agent}")
        if state.status == "completed":
            return state
        

        workflow_state = WorkflowState(**state.dict())
        result = await pm_agent.validate_implementation(workflow_state)
        if result.validation_result == "PASS":
            result.status = "completed"
        return result.dict()

    async def done_node(state: Dict) -> Dict:
        print("Workflow completed successfully.")
        return {} 

    # Add nodes
    workflow.add_node("product_manager", product_manager_node)
    workflow.add_node("developer", developer_node)
    workflow.add_node("reviewer", reviewer_node)
    workflow.add_node("tester", tester_node)
    workflow.add_node("fix_issues", fix_issues_node)
    workflow.add_node("validate", validate_node)
    workflow.add_node("done", done_node)
    
    


    # Add edges
    workflow.add_edge("product_manager", "developer")
    workflow.add_edge("developer", "reviewer")
    workflow.add_edge("fix_issues", "reviewer")
    workflow.add_edge("tester", "validate")
    # workflow.add_edge("validate", "validate")  # Self-loop for termination
    
    # Add conditional edges
    workflow.add_conditional_edges(
        "reviewer",
        after_review,
        {
            "fix_issues": "fix_issues",
            "tester": "tester"
        }
    )
    
    workflow.add_conditional_edges(
        "validate",
        after_validate,
        {
            "developer": "developer",
            "done": "done"  # Self-loop for termination
        }
    )
    
    workflow.set_entry_point("product_manager")
    workflow.set_finish_point("done")
    print("Workflow Nodes:", workflow.edges)
    

    # Compile and return the workflow
    return workflow.compile()