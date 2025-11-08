"""
Pixel Art Homepage Display
ASCII/ANSI art for retro terminal aesthetic
"""

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.table import Table


def display_homepage(console: Console, auth_mode: str = "demo"):
    """Display the pixel art homepage with auth mode"""
    
    # Main ASCII art logo - Large AWS with TERMINAL below
    console.print()
    console.print("╔═══════════════════════════════════════════════════════════════╗", style="bold cyan")
    console.print("║                                                               ║", style="cyan")
    
    # Large AWS text
    line1 = Text()
    line1.append("║       ", style="cyan")
    line1.append("█████╗ ", style="bold yellow")
    line1.append("██╗    ██╗", style="bold orange3")
    line1.append(" ███████╗", style="bold red")
    line1.append("                ║", style="cyan")
    console.print(line1)
    
    line2 = Text()
    line2.append("║      ", style="cyan")
    line2.append("██╔══██╗", style="bold yellow")
    line2.append("██║    ██║", style="bold orange3")
    line2.append(" ██╔════╝", style="bold red")
    line2.append("                ║", style="cyan")
    console.print(line2)
    
    line3 = Text()
    line3.append("║      ", style="cyan")
    line3.append("███████║", style="bold yellow")
    line3.append("██║ █╗ ██║", style="bold orange3")
    line3.append(" ███████╗", style="bold red")
    line3.append("                ║", style="cyan")
    console.print(line3)
    
    line4 = Text()
    line4.append("║      ", style="cyan")
    line4.append("██╔══██║", style="bold yellow")
    line4.append("██║███╗██║", style="bold orange3")
    line4.append(" ╚════██║", style="bold red")
    line4.append("                ║", style="cyan")
    console.print(line4)
    
    line5 = Text()
    line5.append("║      ", style="cyan")
    line5.append("██║  ██║", style="bold yellow")
    line5.append("╚███╔███╔╝", style="bold orange3")
    line5.append(" ███████║", style="bold red")
    line5.append("                ║", style="cyan")
    console.print(line5)
    
    line6 = Text()
    line6.append("║      ", style="cyan")
    line6.append("╚═╝  ╚═╝", style="bold yellow")
    line6.append(" ╚══╝╚══╝ ", style="bold orange3")
    line6.append(" ╚══════╝", style="bold red")
    line6.append("                ║", style="cyan")
    console.print(line6)
    
    console.print("║                                                               ║", style="cyan")
    
    # TERMINAL text - smaller below AWS
    line7 = Text()
    line7.append("║             ", style="cyan")
    line7.append("╔════════════════════════╗", style="bold white")
    line7.append("              ║", style="cyan")
    console.print(line7)
    
    line8 = Text()
    line8.append("║             ", style="cyan")
    line8.append("║  ", style="bold white")
    line8.append("T E R M I N A L", style="bold green")
    line8.append("  ║", style="bold white")
    line8.append("              ║", style="cyan")
    console.print(line8)
    
    line9 = Text()
    line9.append("║             ", style="cyan")
    line9.append("╚════════════════════════╝", style="bold white")
    line9.append("              ║", style="cyan")
    console.print(line9)
    
    console.print("║                                                               ║", style="cyan")
    console.print("║         🤖 AI-Powered Smart Terminal v1.0 ☁️                 ║", style="bold white")
    console.print("║                                                               ║", style="cyan")
    console.print("╚═══════════════════════════════════════════════════════════════╝", style="bold cyan")
    console.print()


def display_mini_cloud():
    """Return a mini cloud ASCII art"""
    return """
    ☁️  ☁️
  ☁️      ☁️
    """


def display_loading_animation(console: Console, message: str = "Processing"):
    """Display a simple loading message"""
    from rich.spinner import Spinner
    from rich.live import Live
    import time
    
    with Live(Spinner("dots", text=f"[cyan]{message}...[/cyan]"), console=console):
        time.sleep(0.5)


def display_success_box(console: Console, message: str):
    """Display a success message in a box"""
    text = Text()
    text.append("✓ ", style="bold green")
    text.append(message, style="white")
    console.print(Panel(text, border_style="green", expand=False))


def display_error_box(console: Console, message: str):
    """Display an error message in a box"""
    text = Text()
    text.append("✗ ", style="bold red")
    text.append(message, style="white")
    console.print(Panel(text, border_style="red", expand=False))


def display_info_box(console: Console, message: str):
    """Display an info message in a box"""
    text = Text()
    text.append("ℹ ", style="bold blue")
    text.append(message, style="white")
    console.print(Panel(text, border_style="blue", expand=False))
