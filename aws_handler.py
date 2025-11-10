"""
AWS Handler
Checks AWS CLI authentication and configuration
"""

import os
import subprocess
from typing import Dict, Any


class AWSHandler:
    """Handler for AWS CLI authentication check"""
    
    def __init__(self, credentials=None):
        """Initialize AWS handler"""
        if credentials:
            self.auth_method = credentials.get('auth_method', 'demo').lower()
            self.aws_profile = credentials.get('aws_profile')
            self.aws_region = credentials.get('aws_region', 'us-east-1')
        else:
            # Fallback to environment variables
            self.auth_method = os.getenv('AWS_AUTH_METHOD', 'demo').lower()
            self.aws_profile = os.getenv('AWS_PROFILE')
            self.aws_region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
        
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
                cmd = ["aws", "sts", "get-caller-identity"]
                if self.aws_profile:
                    cmd.extend(["--profile", self.aws_profile])
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode != 0:
                    print(f"\n⚠️  AWS CLI not configured for profile: {self.aws_profile or 'default'}!")
                    if self.aws_profile:
                        print(f"🔧 Please run: aws configure --profile {self.aws_profile}")
                    else:
                        print("🔧 Please run: aws configure")
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
