"""
Gemini API Handler
Natural language interpretation and command conversion
"""

import os
import json
import google.generativeai as genai
from typing import Dict, Any


class GeminiHandler:
    """Handler for Gemini API interactions"""
    
    def __init__(self):
        """Initialize Gemini API"""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # System prompt for AWS CLI command generation
        self.system_context = """You are an AI assistant specialized in AWS CLI commands. 
Your task is to interpret natural language commands and convert them into AWS CLI commands.

If the command contains MULTIPLE tasks or operations, create a JSON object with "multiple_tasks": true and list all CLI commands.
If the command is a SINGLE task, create a regular JSON object with the CLI command.

For SINGLE tasks, respond with:
{
    "cli_command": "aws [service] [command] [options]",
    "description": "brief description of what this command does"
}

For MULTIPLE tasks, respond with:
{
    "multiple_tasks": true,
    "commands": [
        {
            "cli_command": "aws [service] [command] [options]",
            "description": "what this step does"
        },
        {
            "cli_command": "aws [service] [command] [options]",
            "description": "what this step does"
        }
    ],
    "description": "Overall description of all tasks"
}

Examples:
- "list all S3 buckets" -> {"cli_command": "aws s3 ls", "description": "List all S3 buckets"}
- "create an S3 bucket called my-bucket" -> {"cli_command": "aws s3 mb s3://my-bucket", "description": "Create S3 bucket named my-bucket"}
- "list EC2 instances" -> {"cli_command": "aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,PublicIpAddress]' --output table", "description": "List all EC2 instances"}
- "launch t2.micro instance" -> {"cli_command": "aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --instance-type t2.micro --count 1", "description": "Launch a t2.micro EC2 instance"}
- "start instance i-1234567890" -> {"cli_command": "aws ec2 start-instances --instance-ids i-1234567890", "description": "Start EC2 instance i-1234567890"}
- "create EC2 and security group" -> {"multiple_tasks": true, "commands": [{"cli_command": "aws ec2 create-security-group --group-name my-sg --description 'My security group'", "description": "Create security group"}, {"cli_command": "aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --instance-type t2.micro --security-groups my-sg", "description": "Launch EC2 with security group"}], "description": "Create EC2 instance with security group"}

CRITICAL RULES: 
- Always respond with ONLY valid JSON, no additional text or explanation.
- Use proper AWS CLI syntax with correct service names and commands.
- NEVER use placeholders like <INSTANCE_ID> or <BUCKET_NAME> in commands.
- If specific values are missing (like instance ID), return an error with "missing_info" field listing what's needed.
- Include --output table or --output json where appropriate for better readability.
- Use --query for filtering output when listing resources.
- For commands requiring specific IDs, the user MUST provide them in the command.
"""
    
    def interpret_command(self, user_command: str) -> Dict[str, Any]:
        """
        Interpret natural language command and convert to AWS CLI command
        
        Args:
            user_command: Natural language command from user
            
        Returns:
            Dictionary with cli_command and description
        """
        try:
            # Create the full prompt
            prompt = f"{self.system_context}\n\nUser command: {user_command}\n\nJSON response:"
            
            # Generate response
            response = self.model.generate_content(prompt)
            
            # Parse the response
            response_text = response.text.strip()
            
            # Remove markdown code blocks if present
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            response_text = response_text.strip()
            
            # Parse JSON
            command_data = json.loads(response_text)
            
            return command_data
            
        except json.JSONDecodeError as e:
            return {
                "error": True,
                "cli_command": "",
                "description": f"Failed to parse AI response: {str(e)}\nRaw response: {response_text[:200]}"
            }
        except Exception as e:
            return {
                "error": True,
                "cli_command": "",
                "description": f"Gemini API error: {str(e)}"
            }
    
    def get_help_response(self, question: str) -> str:
        """
        Get help/explanation for a question
        
        Args:
            question: User's question
            
        Returns:
            Helpful response text
        """
        try:
            help_prompt = f"""You are a helpful AWS expert assistant. 
Answer the following question clearly and concisely, focusing on AWS services and best practices.
Keep the response under 300 words.

Question: {question}

Answer:"""
            
            response = self.model.generate_content(help_prompt)
            return response.text.strip()
            
        except Exception as e:
            return f"Error getting help: {str(e)}"
    
    def explain_error(self, error_message: str, context: str = "") -> str:
        """
        Get explanation and suggestions for an error
        
        Args:
            error_message: The error message received
            context: Additional context about what was being attempted
            
        Returns:
            Explanation and suggested fixes
        """
        try:
            prompt = f"""You are an AWS troubleshooting expert.
Explain the following error and provide actionable solutions.
Keep the response concise and practical.

Context: {context}
Error: {error_message}

Explanation and solutions:"""
            
            response = self.model.generate_content(prompt)
            return response.text.strip()
            
        except Exception as e:
            return f"Could not generate error explanation: {str(e)}"
    
    def suggest_completions(self, partial_command: str) -> list:
        """
        Suggest command completions based on partial input
        
        Args:
            partial_command: Incomplete command from user
            
        Returns:
            List of suggested completions
        """
        try:
            prompt = f"""Given this partial AWS command, suggest 5 possible completions.
Return ONLY a JSON array of strings, no other text.

Partial command: {partial_command}

Suggestions (JSON array):"""
            
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Clean up response
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            suggestions = json.loads(response_text.strip())
            
            return suggestions if isinstance(suggestions, list) else []
            
        except Exception as e:
            return []
