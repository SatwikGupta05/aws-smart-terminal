"""
AWS Handler
Checks AWS CLI authentication and configuration
"""

import os
import subprocess
from typing import Dict, Any


class AWSHandler:
    """Handler for AWS CLI authentication check"""
    
    def __init__(self):
        """Initialize AWS handler"""
        self.auth_method = os.getenv('AWS_AUTH_METHOD', 'iam').lower()
        self.check_aws_cli()
    
    def check_aws_cli(self):
        """Check if AWS CLI is installed and configured"""
        try:
            # Check if AWS CLI is installed
            result = subprocess.run(
                ["aws", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                print("\n⚠️  AWS CLI not found!")
                print("📥 Please install AWS CLI: https://aws.amazon.com/cli/")
                raise RuntimeError("AWS CLI not installed")
            
            # Check if AWS is configured (unless in demo mode)
            if self.auth_method != 'demo':
                result = subprocess.run(
                    ["aws", "sts", "get-caller-identity"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode != 0:
                    print("\n⚠️  AWS CLI not configured!")
                    print("🔧 Please run: aws configure")
                    print("   Or set AWS credentials in your .env file and run: aws configure")
                    raise RuntimeError("AWS CLI not configured")
            
        except FileNotFoundError:
            print("\n⚠️  AWS CLI not found!")
            print("📥 Please install AWS CLI: https://aws.amazon.com/cli/")
            raise RuntimeError("AWS CLI not installed")
        except subprocess.TimeoutExpired:
            print("\n⚠️  AWS CLI command timed out")
            raise RuntimeError("AWS CLI timeout")
    
    def is_demo_mode(self) -> bool:
        """Check if running in demo mode"""
        return self.auth_method == 'demo'
    
    def get_auth_status(self) -> Dict[str, Any]:
        """Get authentication status information"""
        if self.auth_method == 'demo':
            return {
                "authenticated": False,
                "mode": "demo",
                "message": "Demo Mode (No AWS Connection)"
            }
        
        try:
            result = subprocess.run(
                ["aws", "sts", "get-caller-identity", "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                import json
                identity = json.loads(result.stdout)
                return {
                    "authenticated": True,
                    "mode": self.auth_method,
                    "user_id": identity.get("UserId", "Unknown"),
                    "account": identity.get("Account", "Unknown"),
                    "arn": identity.get("Arn", "Unknown"),
                    "message": f"Authenticated as {self.auth_method.upper()}"
                }
            else:
                return {
                    "authenticated": False,
                    "mode": self.auth_method,
                    "message": "Authentication failed"
                }
        except Exception as e:
            return {
                "authenticated": False,
                "mode": self.auth_method,
                "message": f"Error: {str(e)}"
            }
