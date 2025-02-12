import google.generativeai as genai
from typing import Any, Dict
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiWrapper:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-pro')
        
    async def generate_response(self, prompt: str, context: Dict[str, Any] = None) -> str:
        """
        Generate a response using Gemini
        """
        try:
            if context:
                prompt = f"Context: {context}\n\nPrompt: {prompt}"
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}" 