"""
Example Usage and Test Cases
Demonstrates the AI-Powered AWS Smart Terminal capabilities
"""

# This file contains examples of how to use the terminal
# Run the actual terminal with: python main.py

EXAMPLES = {
    "natural_language_commands": [
        # S3 Examples
        "list all S3 buckets",
        "create an S3 bucket called my-test-bucket",
        "upload readme.txt to my-test-bucket",
        "list files in my-test-bucket",
        "download data.csv from my-test-bucket",
        
        # EC2 Examples
        "show me all EC2 instances",
        "launch a t2.micro EC2 instance",
        "stop EC2 instance i-1234567890abcdef0",
        "start EC2 instance i-1234567890abcdef0",
        
        # Lambda Examples
        "list all Lambda functions",
        "invoke Lambda function my-data-processor",
        
        # Multi-service Examples
        "show all my RDS databases",
        "list IAM users",
        "what DynamoDB tables do I have",
        "show SNS topics",
        "list SQS queues",
    ],
    
    "shell_commands": [
        "!dir",
        "!cd Documents",
        "!pwd",
        "!python --version",
        "!pip list",
        "!git status",
        "!echo Hello AWS Terminal",
        "!type README.md",
    ],
    
    "help_queries": [
        "?what is S3",
        "?how do I create an EC2 instance",
        "?explain Lambda functions",
        "?S3 security best practices",
        "?how to reduce AWS costs",
        "?what are EC2 instance types",
        "?how does IAM work",
    ],
    
    "special_commands": [
        "home",
        "history",
        "clear",
        "exit",
    ]
}

# Expected behavior for each command type:
# 
# NATURAL LANGUAGE:
# 1. User types plain English command
# 2. Terminal shows "Processing: [command]"
# 3. AI interprets command (shows service, action, parameters)
# 4. Executes on AWS
# 5. Displays results in formatted table/list
#
# SHELL COMMANDS (! prefix):
# 1. User types !command
# 2. Terminal shows "Executing shell command: [command]"
# 3. Runs in PowerShell (Windows) or bash (Linux/Mac)
# 4. Shows stdout/stderr output
#
# HELP QUERIES (? prefix):
# 1. User types ?question
# 2. Terminal shows "Getting help for: [question]"
# 3. AI generates helpful response
# 4. Displays in formatted panel
#
# SPECIAL COMMANDS:
# 1. Direct action (clear screen, show history, exit, etc.)
# 2. No AI processing needed

def print_examples():
    """Print all examples for reference"""
    print("=" * 60)
    print("AI-POWERED AWS SMART TERMINAL - EXAMPLE COMMANDS")
    print("=" * 60)
    
    print("\n📝 NATURAL LANGUAGE COMMANDS")
    print("-" * 60)
    for cmd in EXAMPLES["natural_language_commands"]:
        print(f"  > {cmd}")
    
    print("\n⚡ SHELL COMMANDS (! prefix)")
    print("-" * 60)
    for cmd in EXAMPLES["shell_commands"]:
        print(f"  > {cmd}")
    
    print("\n❓ HELP QUERIES (? prefix)")
    print("-" * 60)
    for cmd in EXAMPLES["help_queries"]:
        print(f"  > {cmd}")
    
    print("\n🔧 SPECIAL COMMANDS")
    print("-" * 60)
    for cmd in EXAMPLES["special_commands"]:
        print(f"  > {cmd}")
    
    print("\n" + "=" * 60)
    print("Start the terminal with: python main.py")
    print("=" * 60)

if __name__ == "__main__":
    print_examples()
