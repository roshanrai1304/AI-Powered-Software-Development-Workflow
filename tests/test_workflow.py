import requests
import json

def test_workflow():
    # API endpoint
    url = "http://127.0.0.1:8000/api/v1/workflow/start"
    
    # Test requirements
    requirements = """
    Create a Todo List API with the following features:
    1. CRUD operations for tasks
    2. Task prioritization (High, Medium, Low)

    3. Due date for each task
    4. Task categories/tags
    5. Task completion status
    6. User authentication
    7. API documentation
    
    Technical Requirements:
    - Use FastAPI for the backend
    - PostgreSQL for database
    - JWT for authentication
    - OpenAPI/Swagger documentation
    """
    
    # Request payload
    payload = {
        "requirements": requirements,
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
    
    # Make the request
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        # Print the response in a formatted way
        result = response.json()
        print("\n=== Workflow Result ===\n")
        print("Status:", result["status"])
        print("Message:", result["message"])
        print("\n=== Workflow Data ===\n")
        
        # Print each stage of the workflow
        data = result["data"]
        
        if "user_story" in data:
            print("\n--- User Story ---\n")
            print(data["user_story"])
            
        if "code" in data:
            print("\n--- Implementation ---\n")
            print(data["code"])
            
        if "review_feedback" in data:
            print("\n--- Code Review ---\n")
            print(data["review_feedback"])
            
        if "test_results" in data:
            print("\n--- Test Results ---\n")
            print(data["test_results"])
            
        if "validation_result" in data:
            print("\n--- Final Validation ---\n")
            print(data["validation_result"])
            
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        
if __name__ == "__main__":
    test_workflow() 