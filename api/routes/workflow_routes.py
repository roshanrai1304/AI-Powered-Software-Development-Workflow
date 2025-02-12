from fastapi import APIRouter, HTTPException, status
from api.models.request_models import RequirementsRequest, WorkflowResponse, WorkflowStage
from workflows.workflow_state import WorkflowState
from workflows.development_workflow import create_workflow
import asyncio


router = APIRouter()

@router.post(
    "/workflow/start",
    response_model=WorkflowResponse,
    status_code=status.HTTP_201_CREATED,
    response_description="Workflow started successfully"
)
async def start_workflow(request: RequirementsRequest):
    try:
        workflow = create_workflow()
        # Create initial state with only necessary fields
        initial_state = {
            "requirements": request.requirements,
            "context": request.context.dict() if request.context else None,
            "user_story": None,
            "code": None,
            "review_feedback": None,
            "test_results": None,
            "validation_result": None,
            "status": None,
            "current_agent": "product_manager"  # Set initial agent
        }

        print(f"initial_state: {initial_state}")
        workflow = create_workflow()
        

        final_state = await workflow.ainvoke(initial_state)

        print(f"final_state: {final_state}")
        
        # Create workflow stages from the final state
        stages = []
        stage_mapping = {
            "product_manager": "product_manager",
            "developer": "developer",
            "reviewer": "reviewer",
            "tester": "tester"
        }

        for node_name, stage_name in stage_mapping.items():
            if node_name in final_state:
                stages.append(
                    WorkflowStage(
                        name=stage_name,
                        status="completed",
                        output=final_state[node_name]
                    )
                )
        
        return WorkflowResponse(
            status="success",
            message="Workflow completed successfully",
            data=final_state,
            stages=stages
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error executing workflow: {str(e)}"
        )

@router.get("/workflow/status/{workflow_id}")
async def get_workflow_status(workflow_id: str):
    # This is a placeholder for workflow status tracking
    # You would need to implement actual status tracking
    return {
        "workflow_id": workflow_id,
        "status": "in_progress"
    } 