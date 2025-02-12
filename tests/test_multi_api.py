import asyncio
import requests
from rich import print
from rich.console import Console
from rich.panel import Panel
from typing import Dict, Any

console = Console()

async def test_multiple_apis():
    base_url = "http://127.0.0.1:8000/api/v1"
    
    test_cases = [
        {
            "name": "Authentication Service",
            "requirements": """
            Create an Authentication Service with:
            1. User Management
                - Registration with email verification
                - Login with JWT tokens
                - Password reset functionality
                - OAuth2 integration (Google, GitHub)
            2. Security Features
                - Two-factor authentication
                - Role-based access control
                - Session management
                - Rate limiting
            3. API Integration
                - RESTful endpoints
                - OpenAPI documentation
                - SDK generation
            """,
            "context": {
                "project_type": "backend",
                "tech_stack": ["FastAPI", "PostgreSQL", "Redis", "JWT"],
                "priority": "high",
                "security_requirements": ["HTTPS", "OAuth2", "2FA"]
            }
        },
        {
            "name": "Real-time Chat Service",
            "requirements": """
            Build a Real-time Chat Service with:
            1. Messaging Features
                - One-on-one messaging
                - Group chats
                - File sharing
                - Message history
            2. Real-time Features
                - Online status
                - Typing indicators
                - Read receipts
                - Push notifications
            3. Data Management
                - Message persistence
                - User profiles
                - Chat history
            """,
            "context": {
                "project_type": "full-stack",
                "tech_stack": ["FastAPI", "WebSocket", "MongoDB", "Redis"],
                "priority": "medium",
                "performance_requirements": {
                    "max_latency": "50ms",
                    "concurrent_users": 10000
                }
            }
        }
    ]
    
    async def process_test_case(test_case: Dict[str, Any]):
        console.print(f"\n[bold blue]Testing {test_case['name']}[/bold blue]")
        console.print(Panel.fit(test_case['requirements'], title="Requirements"))
        
        payload = {
            "requirements": test_case["requirements"],
            "context": test_case["context"]
        }
        
        try:
            with console.status(f"[bold green]Processing {test_case['name']}...") as status:
                response = requests.post(f"{base_url}/workflow/start", json=payload)
                response.raise_for_status()
                result = response.json()
                
                console.print(f"\n[bold green]Status:[/bold green] {result['status']}")
                console.print(f"[bold green]Message:[/bold green] {result['message']}\n")
                
                # Print stages
                for stage in result.get('stages', []):
                    console.print(Panel(
                        f"[bold]Status:[/bold] {stage['status']}\n\n{json.dumps(stage.get('output', {}), indent=2)}",
                        title=f"[bold blue]{stage['name'].upper()}[/bold blue]",
                        expand=False
                    ))
                
                return result
                
        except Exception as e:
            console.print(f"[bold red]Error processing {test_case['name']}:[/bold red] {str(e)}")
            return None
    
    results = []
    for test_case in test_cases:
        result = await process_test_case(test_case)
        if result:
            results.append(result)
    
    # Print summary
    console.print("\n[bold blue]Test Summary[/bold blue]")
    for i, result in enumerate(results, 1):
        console.print(f"Test {i}: [green]{result['status']}[/green] - {result['message']}")

if __name__ == "__main__":
    # Install dependencies: pip install rich requests
    asyncio.run(test_multiple_apis()) 