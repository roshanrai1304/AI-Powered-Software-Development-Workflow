import requests
import json
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

def test_simple_api():
    url = "http://127.0.0.1:8000/api/v1/workflow/start"
    
    # A simple API requirement for testing
    requirements = """
    Create a Weather API with the following features:
    1. Current weather data
        - Temperature
        - Humidity
        - Wind speed
        - Weather conditions
    2. Weather forecast
        - 5-day forecast
        - Hourly predictions
    3. Location-based services
        - City lookup
        - Geolocation support
    4. API Features
        - Rate limiting
        - Caching
        - Error handling
        - API documentation
    """
    
    payload = {
        "requirements": requirements,
        "context": {
            "project_type": "backend",
            "tech_stack": ["FastAPI", "Redis", "PostgreSQL"],
            "priority": "high",
            "security_requirements": ["API Key", "Rate Limiting"],
            "performance_requirements": {
                "max_response_time": "100ms",
                "cache_duration": "5min"
            }
        }
    }
    
    try:
        console.print("\n[bold blue]Starting Weather API Workflow Test[/bold blue]")
        console.print(Panel.fit(requirements, title="Requirements"))
        
        with console.status("[bold green]Processing workflow...") as status:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            # Print workflow results
            console.print("\n[bold green]Workflow Completed[/bold green]")
            console.print(f"Status: {result['status']}")
            console.print(f"Message: {result['message']}\n")
            
            # Print each stage with proper formatting
            data = result['data']
            stages = result.get('stages', [])
            
            for stage in stages:
                stage_name = stage['name']
                stage_status = stage['status']
                stage_output = stage.get('output', {})
                
                console.print(Panel(
                    f"[bold]Status:[/bold] {stage_status}\n\n{json.dumps(stage_output, indent=2)}",
                    title=f"[bold blue]{stage_name.upper()}[/bold blue]",
                    expand=False
                ))
                
            return result
            
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        return None

if __name__ == "__main__":
    # Install rich for better output formatting: pip install rich
    test_simple_api() 