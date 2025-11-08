"""
AI-Powered AWS Smart Terminal
Main entry point and terminal loop
"""

import os
import sys
from pathlib import Path
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from dotenv import load_dotenv

from homepage import display_homepage
from command_processor import CommandProcessor
from gemini_handler import GeminiHandler
from aws_handler import AWSHandler

# Load environment variables
load_dotenv()

class AWSSmartTerminal:
    """Main terminal class"""
    
    def __init__(self):
        """Initialize the terminal"""
        self.console = Console()
        self.history_file = os.getenv('HISTORY_FILE', '.terminal_history')
        self.max_history = int(os.getenv('MAX_HISTORY_ENTRIES', 1000))
        
        # Initialize components
        try:
            self.gemini_handler = GeminiHandler()
            self.aws_handler = AWSHandler()
            self.command_processor = CommandProcessor(
                self.gemini_handler, 
                self.aws_handler,
                self.console
            )
        except Exception as e:
            self.console.print(f"[bold red]Error initializing terminal:[/bold red] {str(e)}")
            self.console.print("[yellow]Please check your .env file and ensure all credentials are set correctly.[/yellow]")
            sys.exit(1)
        
        # Setup prompt session with history
        self.session = PromptSession(
            history=FileHistory(self.history_file),
            auto_suggest=AutoSuggestFromHistory(),
        )
        
        self.running = True
    
    def display_welcome(self):
        """Display welcome message and homepage"""
        self.console.clear()
        display_homepage(self.console, self.aws_handler.auth_method)
        
        welcome_text = Text()
        welcome_text.append("\n🚀 AI-Powered AWS Smart Terminal\n", style="bold cyan")
        welcome_text.append("Type commands in natural language, use ", style="white")
        welcome_text.append("!", style="bold yellow")
        welcome_text.append(" for shell, ", style="white")
        welcome_text.append("?", style="bold green")
        welcome_text.append(" for help\n", style="white")
        
        # Display authentication info
        auth_info = Text()
        auth_info.append("🔐 Authenticated as: ", style="dim")
        if self.aws_handler.auth_method == "root":
            auth_info.append(f"{self.aws_handler.auth_method.upper()} ", style="bold red")
            auth_info.append("⚠️  (Not Recommended)", style="yellow")
        elif self.aws_handler.auth_method == "demo":
            auth_info.append("Demo Mode", style="bold yellow")
        else:
            auth_info.append(f"{self.aws_handler.auth_method.upper()} User", style="bold green")
        welcome_text.append(auth_info)
        welcome_text.append("\n", style="white")
        
        welcome_text.append("Commands: ", style="dim")
        welcome_text.append("home", style="bold")
        welcome_text.append(" | ", style="dim")
        welcome_text.append("history", style="bold")
        welcome_text.append(" | ", style="dim")
        welcome_text.append("clear", style="bold")
        welcome_text.append(" | ", style="dim")
        welcome_text.append("exit", style="bold")
        welcome_text.append("\n", style="dim")
        
        self.console.print(Panel(welcome_text, border_style="cyan"))
    
    def get_prompt_string(self):
        """Generate the prompt string"""
        return [
            ('class:username', '⚡ AWS'),
            ('class:at', ' ➜ '),
            ('class:path', ''),
        ]
    
    def run(self):
        """Main terminal loop"""
        self.display_welcome()
        
        while self.running:
            try:
                # Get user input with colored prompt
                user_input = self.session.prompt(
                    self.get_prompt_string(),
                    style=self._get_prompt_style()
                ).strip()
                
                # Skip empty input
                if not user_input:
                    continue
                
                # Process the command
                result = self.command_processor.process_command(user_input)
                
                # Handle special return values
                if result == "EXIT":
                    self.running = False
                elif result == "CLEAR":
                    self.console.clear()
                elif result == "HOME":
                    self.console.clear()
                    display_homepage(self.console)
                elif result == "HISTORY":
                    self._display_history()
                    
            except KeyboardInterrupt:
                # Ctrl+C pressed
                self.console.print("\n[yellow]Use 'exit' or 'quit' to leave the terminal[/yellow]")
                continue
            except EOFError:
                # Ctrl+D pressed
                self.running = False
                break
            except Exception as e:
                self.console.print(f"[bold red]Error:[/bold red] {str(e)}")
        
        self._goodbye()
    
    def _get_prompt_style(self):
        """Return the style for the prompt"""
        from prompt_toolkit.styles import Style
        return Style.from_dict({
            'username': '#00ff00 bold',
            'at': '#00ffff',
            'path': '#ffff00',
        })
    
    def _display_history(self):
        """Display command history"""
        history_file = Path(self.history_file)
        
        if not history_file.exists():
            self.console.print("[yellow]No command history yet[/yellow]")
            return
        
        with open(history_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            self.console.print("[yellow]No command history yet[/yellow]")
            return
        
        self.console.print("\n[bold cyan]Command History:[/bold cyan]")
        for i, line in enumerate(lines[-20:], start=max(1, len(lines) - 19)):
            self.console.print(f"  [dim]{i:3d}[/dim] {line.strip()}")
        self.console.print()
    
    def _goodbye(self):
        """Display goodbye message"""
        goodbye_text = Text()
        goodbye_text.append("\n👋 ", style="bold")
        goodbye_text.append("Thanks for using AWS Smart Terminal!", style="bold cyan")
        goodbye_text.append("\n🌟 Stay cloudy! ☁️\n", style="yellow")
        
        self.console.print(Panel(goodbye_text, border_style="cyan"))


def main():
    """Entry point"""
    terminal = AWSSmartTerminal()
    terminal.run()


if __name__ == "__main__":
    main()
