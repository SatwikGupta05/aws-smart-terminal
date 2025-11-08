"""
Command Processor
Routes and executes commands (natural language, shell, help)
"""

import subprocess
import sys
from typing import Optional
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table
from rich.panel import Panel

from gemini_handler import GeminiHandler
from aws_handler import AWSHandler
from homepage import display_success_box, display_error_box, display_info_box


class CommandProcessor:
    """Process and route different types of commands"""
    
    def __init__(self, gemini_handler: GeminiHandler, aws_handler: AWSHandler, console: Console):
        """Initialize the command processor"""
        self.gemini = gemini_handler
        self.aws = aws_handler
        self.console = console
    
    def process_command(self, command: str) -> Optional[str]:
        """
        Process a command and route to appropriate handler
        
        Args:
            command: User command string
            
        Returns:
            Special command result (EXIT, CLEAR, HOME, HISTORY) or None
        """
        command = command.strip()
        
        # Check for special commands
        if command.lower() in ['exit', 'quit', 'bye']:
            return "EXIT"
        
        if command.lower() in ['clear', 'cls']:
            return "CLEAR"
        
        if command.lower() in ['home', 'homepage']:
            return "HOME"
        
        if command.lower() == 'history':
            return "HISTORY"
        
        # Route based on prefix
        if command.startswith('!'):
            # Shell command
            self._execute_shell_command(command[1:].strip())
        elif command.startswith('?'):
            # Help/question
            self._execute_help_command(command[1:].strip())
        else:
            # Natural language AWS command
            self._execute_aws_command(command)
        
        return None
    
    def _execute_shell_command(self, command: str):
        """Execute a shell command"""
        if not command:
            self.console.print("[yellow]No shell command provided[/yellow]")
            return
        
        self.console.print(f"[dim]Executing shell command:[/dim] [cyan]{command}[/cyan]")
        
        try:
            # Execute command using PowerShell on Windows
            if sys.platform == "win32":
                result = subprocess.run(
                    ["powershell", "-Command", command],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
            else:
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
            
            # Display output
            if result.stdout:
                self.console.print(result.stdout)
            
            if result.stderr:
                self.console.print(f"[yellow]{result.stderr}[/yellow]")
            
            if result.returncode != 0:
                self.console.print(f"[red]Command exited with code {result.returncode}[/red]")
                
        except subprocess.TimeoutExpired:
            self.console.print("[red]Command timed out after 30 seconds[/red]")
        except Exception as e:
            self.console.print(f"[red]Error executing command: {str(e)}[/red]")
    
    def _execute_help_command(self, question: str):
        """Get help from Gemini AI"""
        if not question:
            self._show_general_help()
            return
        
        self.console.print(f"[dim]Getting help for:[/dim] [cyan]{question}[/cyan]\n")
        
        try:
            # Get response from Gemini
            response = self.gemini.get_help_response(question)
            
            # Display in a nice panel
            self.console.print(Panel(
                response,
                title="💡 AI Assistant",
                border_style="green",
                padding=(1, 2)
            ))
            
        except Exception as e:
            display_error_box(self.console, f"Failed to get help: {str(e)}")
    
    def _execute_aws_command(self, command: str):
        """Execute a natural language AWS command"""
        self.console.print(f"[dim]Processing:[/dim] [cyan]{command}[/cyan]")
        
        try:
            # Step 1: Interpret with Gemini to get AWS CLI command
            self.console.print("[dim]🤖 AI generating AWS CLI command...[/dim]")
            interpretation = self.gemini.interpret_command(command)
            
            # Check for errors
            if interpretation.get('error'):
                display_error_box(self.console, interpretation.get('description', 'Unknown error'))
                return
            
            # Check if information is missing
            if interpretation.get('missing_info'):
                missing = interpretation.get('missing_info')
                self.console.print(f"[yellow]⚠️  Missing information:[/yellow]")
                # If it's a list, iterate through items
                if isinstance(missing, list):
                    for info in missing:
                        self.console.print(f"   • {info}")
                # If it's a string, just print it
                else:
                    self.console.print(f"   • {missing}")
                self.console.print("\n[dim]Please provide the required information in your command.[/dim]")
                return
            
            # Check if this is a multi-task request
            if interpretation.get('multiple_tasks'):
                self.console.print(f"[dim]→ Multiple tasks detected:[/dim] [yellow]{interpretation.get('description', 'Multiple operations')}[/yellow]")
                commands = interpretation.get('commands', [])
                
                # Display all commands first
                self.console.print("\n[bold]Commands to be executed:[/bold]")
                for i, cmd_info in enumerate(commands, 1):
                    cli_cmd = cmd_info.get('cli_command', '')
                    desc = cmd_info.get('description', '')
                    self.console.print(f"  [bold cyan]{i}.[/bold cyan] [dim]{desc}[/dim]")
                    self.console.print(f"     [yellow]{cli_cmd}[/yellow]")
                
                # Ask for confirmation
                self.console.print()
                confirm = input("⚠️  Execute these commands on AWS? (y/n): ").strip().lower()
                if confirm != 'y':
                    self.console.print("[yellow]⚠️  Commands cancelled[/yellow]")
                    return
                
                # Step 2: Execute each CLI command
                self.console.print("\n[dim]☁️ Executing AWS CLI commands...[/dim]\n")
                for i, cmd_info in enumerate(commands, 1):
                    cli_cmd = cmd_info.get('cli_command', '')
                    desc = cmd_info.get('description', '')
                    
                    self.console.print(f"[bold cyan]Step {i}:[/bold cyan] [dim]{desc}[/dim]")
                    self._execute_cli_command(cli_cmd)
                    self.console.print()
            else:
                # Single task - Display interpretation
                cli_cmd = interpretation.get('cli_command', '')
                desc = interpretation.get('description', '')
                
                self.console.print(f"[dim]→ Description:[/dim] [yellow]{desc}[/yellow]")
                self.console.print(f"[dim]→ CLI Command:[/dim] [yellow]{cli_cmd}[/yellow]")
                self.console.print()
                
                # Ask for confirmation before executing
                confirm = input("⚠️  Execute this command on AWS? (y/n): ").strip().lower()
                if confirm != 'y':
                    self.console.print("[yellow]⚠️  Command cancelled[/yellow]")
                    return
                
                # Step 2: Execute AWS CLI command
                self.console.print("[dim]☁️ Executing AWS CLI command...[/dim]")
                self._execute_cli_command(cli_cmd)
                
        except Exception as e:
            display_error_box(self.console, f"Command execution failed: {str(e)}")
    
    def _execute_cli_command(self, cli_command: str):
        """Execute an AWS CLI command and display results"""
        if not cli_command:
            display_error_box(self.console, "No CLI command generated")
            return
        
        try:
            # Execute AWS CLI command
            if sys.platform == "win32":
                result = subprocess.run(
                    ["powershell", "-Command", cli_command],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
            else:
                result = subprocess.run(
                    cli_command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=60
                )
            
            # Display output
            if result.returncode == 0:
                display_success_box(self.console, "Command executed successfully")
                if result.stdout:
                    self.console.print("\n[bold]Output:[/bold]")
                    self.console.print(result.stdout)
            else:
                display_error_box(self.console, f"Command failed with exit code {result.returncode}")
                if result.stderr:
                    self.console.print(f"\n[red]{result.stderr}[/red]")
                    
        except subprocess.TimeoutExpired:
            display_error_box(self.console, "Command timed out after 60 seconds")
        except Exception as e:
            display_error_box(self.console, f"Error executing CLI command: {str(e)}")
    
    def _display_data(self, data, service: str):
        """Display command output data in a formatted way"""
        if not data:
            return
        
        self.console.print()
        
        # If it's a list of strings, display as a simple list
        if isinstance(data, list) and all(isinstance(item, str) for item in data):
            for item in data:
                self.console.print(f"  • [cyan]{item}[/cyan]")
        
        # If it's a list of dictionaries (like EC2 instances), display as table
        elif isinstance(data, list) and data and isinstance(data[0], dict):
            table = Table(show_header=True, header_style="bold cyan")
            
            # Add columns based on first item
            for key in data[0].keys():
                table.add_column(key.upper())
            
            # Add rows
            for item in data:
                table.add_row(*[str(item[key]) for key in data[0].keys()])
            
            self.console.print(table)
        
        # If it's a dictionary, display as key-value pairs
        elif isinstance(data, dict):
            for key, value in data.items():
                self.console.print(f"  [yellow]{key}:[/yellow] [cyan]{value}[/cyan]")
        
        self.console.print()
    

    def _show_general_help(self):
        """Show general help information"""
        help_text = """
[bold cyan]AWS Smart Terminal - Help Guide[/bold cyan]

[bold yellow]Command Types:[/bold yellow]

[bold green]1. Natural Language Commands[/bold green]
   Just type what you want to do in plain English:
   • list all S3 buckets
   • create an EC2 instance with t2.micro
   • show me all Lambda functions
   • upload myfile.txt to my-bucket

[bold green]2. Shell Commands (prefix with !)[/bold green]
   Execute any shell command:
   • !dir or !ls
   • !cd Documents
   • !python --version
   • !git status

[bold green]3. Help/Questions (prefix with ?)[/bold green]
   Ask questions about AWS:
   • ?how do I create an S3 bucket
   • ?what are EC2 instance types
   • ?explain Lambda functions

[bold yellow]Special Commands:[/bold yellow]
   • home, homepage  - Show the pixel art homepage
   • history         - Display command history
   • clear, cls      - Clear the terminal screen
   • exit, quit      - Exit the terminal

[bold yellow]Supported AWS Services:[/bold yellow]
   EC2, S3, Lambda, RDS, IAM, CloudWatch, DynamoDB, SNS, SQS

[bold yellow]Navigation:[/bold yellow]
   • Use ↑/↓ arrow keys to browse command history
   • Press Tab for auto-completion (coming soon)
   • Press Ctrl+C to cancel current input
   • Press Ctrl+D to exit
"""
        self.console.print(help_text)
