import requests
import json
import asyncio
from typing import Dict, Any

async def test_complex_workflow():
    # API endpoint
    base_url = "http://127.0.0.1:8000/api/v1"
    
    # Test cases with different requirements
    test_cases = [
        {
            "name": "E-commerce API",
            "requirements": """
            Create an E-commerce REST API with:
            1. Product management
                - CRUD operations
                - Product categories
                - Product search
                - Product reviews
            2. Shopping Cart
                - Add/remove items
                - Update quantities
                - Calculate totals
            3. Order Management
                - Place orders
                - Order history
                - Order status tracking
            4. User Management
                - Authentication
                - User profiles
                - Address management
            5. Payment Integration
                - Stripe integration
                - Payment history
            """,
            "context": {
                "project_type": "backend",
                "tech_stack": ["FastAPI", "PostgreSQL", "Redis", "Stripe"],
                "priority": "high",
                "security_requirements": ["HTTPS", "API Keys", "JWT"],
                "performance_requirements": {
                    "max_response_time": "200ms",
                    "concurrent_users": 1000
                }
            }
        },
        {
            "name": "Task Management System",
            "requirements": """
            Build a Task Management API with:
            1. Task Operations
                - Create, read, update, delete tasks
                - Task assignments
                - Task dependencies
                - Priority levels
                - Due dates
            2. Project Management
                - Project creation
                - Team management
                - Project timeline
            3. Collaboration
                - Comments on tasks
                - File attachments
                - Activity tracking
            4. Reporting
                - Task status reports
                - Time tracking
                - Performance metrics
            """,
            "context": {
                "project_type": "full-stack",
                "tech_stack": ["FastAPI", "MongoDB", "Redis", "React"],
                "priority": "medium",
                "deployment": "Docker",
                "monitoring": "Prometheus"
            }
        }
    ]
    
    async def process_test_case(test_case: Dict[str, Any]):
        print(f"\n=== Testing {test_case['name']} ===\n")
        
        payload = {
            "requirements": test_case["requirements"],
            "context": test_case["context"]
        }
        
        try:
            response = requests.post(f"{base_url}/workflow/start", json=payload)
            response.raise_for_status()
            result = response.json()
            
            print(f"Status: {result['status']}")
            print(f"Message: {result['message']}")
            
            if result["status"] == "success":
                data = result["data"]
                
                # Print workflow stages
                stages = [
                    ("User Story", "user_story"),
                    ("Implementation", "code"),
                    ("Code Review", "review_feedback"),
                    ("Test Results", "test_results"),
                    ("Final Validation", "validation_result")
                ]
                
                for stage_name, stage_key in stages:
                    if stage_key in data:
                        print(f"\n--- {stage_name} ---\n")
                        print(data[stage_key])
                        print("\n" + "="*50 + "\n")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"Error processing {test_case['name']}: {e}")
            return None
    
    # Process all test cases
    results = []
    for test_case in test_cases:
        result = await process_test_case(test_case)
        if result:
            results.append(result)
    
    # Print summary
    print("\n=== Test Summary ===\n")
    for i, result in enumerate(results):
        print(f"Test Case {i+1}: {result['status']}")
        print(f"Message: {result['message']}")
        print()

if __name__ == "__main__":
    asyncio.run(test_complex_workflow()) 