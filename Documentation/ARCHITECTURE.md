# 🏗️ Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              prompt_toolkit Terminal                     │   │
│  │  • Command History (↑/↓)                                │   │
│  │  • Auto-suggestions                                      │   │
│  │  • Rich Formatting                                       │   │
│  │  • Colorful Output                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MAIN TERMINAL ENGINE                         │
│                        (main.py)                                │
│                                                                 │
│  • Session Management                                           │
│  • History Persistence                                          │
│  • Event Loop                                                   │
│  • Special Commands (exit, clear, home, history)               │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   COMMAND PROCESSOR                             │
│                 (command_processor.py)                          │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │   Natural    │  │    Shell     │  │     Help     │        │
│  │   Language   │  │   Commands   │  │    Queries   │        │
│  │   (default)  │  │   (! prefix) │  │  (? prefix)  │        │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘        │
│         │                  │                  │                 │
└─────────┼──────────────────┼──────────────────┼─────────────────┘
          │                  │                  │
          │                  │                  │
          ▼                  ▼                  ▼
┌─────────────────┐  ┌─────────────┐  ┌─────────────────┐
│  GEMINI HANDLER │  │  SUBPROCESS │  │  GEMINI HANDLER │
│ (gemini_handler │  │  (shell)    │  │ (gemini_handler │
│      .py)       │  │             │  │      .py)       │
│                 │  │             │  │                 │
│ • Interpret NL  │  │ • Execute   │  │ • Answer Q&A    │
│ • Return JSON   │  │   PowerShell│  │ • Explain       │
│ • Gemini API    │  │ • Capture   │  │ • Guide user    │
│                 │  │   output    │  │                 │
└────────┬────────┘  └─────────────┘  └─────────────────┘
         │
         │ {service, action, parameters}
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AWS HANDLER                                │
│                   (aws_handler.py)                              │
│                                                                 │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐      │
│  │   S3   │ │  EC2   │ │ Lambda │ │  RDS   │ │  IAM   │      │
│  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘      │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐                 │
│  │ CloudW.│ │DynamoDB│ │  SNS   │ │  SQS   │                 │
│  └────────┘ └────────┘ └────────┘ └────────┘                 │
│                                                                 │
│  • Service Router                                               │
│  • boto3 Client Management                                      │
│  • Error Handling                                               │
│  • Response Formatting                                          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AWS CLOUD (boto3)                          │
│                                                                 │
│     ┌─────┐  ┌─────┐  ┌──────┐  ┌─────┐  ┌─────┐            │
│     │ EC2 │  │ S3  │  │Lambda│  │ RDS │  │ IAM │  ...       │
│     └─────┘  └─────┘  └──────┘  └─────┘  └─────┘            │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

### Example: "list all S3 buckets"

```
1. USER INPUT
   ↓
   "list all S3 buckets"

2. MAIN.PY (Terminal Loop)
   ↓
   • Capture input via prompt_toolkit
   • Save to history
   • Pass to command processor

3. COMMAND_PROCESSOR.PY
   ↓
   • Detect: No prefix → Natural language
   • Route to Gemini handler

4. GEMINI_HANDLER.PY
   ↓
   • Send to Gemini API with context
   • Receive interpretation:
     {
       "service": "s3",
       "action": "list_buckets",
       "parameters": {},
       "description": "List all S3 buckets"
     }
   • Return to command processor

5. COMMAND_PROCESSOR.PY
   ↓
   • Display interpretation
   • Pass to AWS handler

6. AWS_HANDLER.PY
   ↓
   • Route to _handle_s3()
   • Action: list_buckets
   • Get boto3 S3 client
   • Call: s3.list_buckets()
   • Format response:
     {
       "success": true,
       "data": ["bucket1", "bucket2", ...],
       "message": "Found 5 bucket(s)"
     }
   • Return to command processor

7. COMMAND_PROCESSOR.PY
   ↓
   • Display success box
   • Format data as list
   • Show to user with colors

8. USER SEES
   ↓
   ✓ Found 5 bucket(s)
   
   • my-bucket-1
   • my-bucket-2
   • my-bucket-3
   • my-bucket-4
   • my-bucket-5
```

## Component Details

### 1. Terminal Interface (main.py)
```python
PromptSession
  ├── FileHistory         # Persistent command history
  ├── AutoSuggest         # Suggestions from history
  └── Custom Styling      # Colors and formatting
```

**Responsibilities:**
- Manage terminal session
- Handle keyboard input (↑/↓ for history)
- Coordinate between modules
- Special command handling
- Display homepage

### 2. Command Processor (command_processor.py)
```python
CommandProcessor
  ├── process_command()           # Main router
  ├── _execute_shell_command()    # Handle ! commands
  ├── _execute_help_command()     # Handle ? commands
  ├── _execute_aws_command()      # Handle natural language
  └── _display_data()             # Format output
```

**Responsibilities:**
- Route commands by type/prefix
- Execute shell commands
- Coordinate Gemini + AWS
- Format and display results

### 3. Gemini Handler (gemini_handler.py)
```python
GeminiHandler
  ├── interpret_command()      # NL → AWS operation
  ├── get_help_response()      # Answer questions
  ├── explain_error()          # Troubleshoot
  └── suggest_completions()    # Auto-complete
```

**Responsibilities:**
- Natural language interpretation
- Q&A and help
- Error explanation
- Command suggestions

### 4. AWS Handler (aws_handler.py)
```python
AWSHandler
  ├── execute_operation()      # Main entry point
  ├── _get_client()            # Lazy client creation
  ├── _handle_s3()             # S3 operations
  ├── _handle_ec2()            # EC2 operations
  ├── _handle_lambda()         # Lambda operations
  └── ... (more services)
```

**Responsibilities:**
- Execute AWS operations
- Manage boto3 clients
- Error handling
- Response formatting

### 5. Homepage (homepage.py)
```python
homepage
  ├── display_homepage()       # Main ASCII art
  ├── display_success_box()    # Success messages
  ├── display_error_box()      # Error messages
  └── display_info_box()       # Info messages
```

**Responsibilities:**
- Visual elements
- ASCII art
- Message boxes
- Status displays

## Configuration Flow

```
.env file
  ├── AWS_ACCESS_KEY_ID       → AWS Handler
  ├── AWS_SECRET_ACCESS_KEY   → AWS Handler
  ├── AWS_DEFAULT_REGION      → AWS Handler
  ├── GEMINI_API_KEY          → Gemini Handler
  ├── HISTORY_FILE            → Main Terminal
  └── MAX_HISTORY_ENTRIES     → Main Terminal
```

## Error Handling Strategy

```
Error at Any Layer
  ↓
Try-Catch Block
  ↓
Return Error Object
  {
    "success": false,
    "error": "descriptive message"
  }
  ↓
Command Processor
  ↓
Display Error Box (Red)
  ✗ Error message
  ↓
Optional: Gemini Explains Error
  ↓
User Sees Clear Feedback
```

## Security Architecture

```
┌──────────────────────┐
│   Environment Vars   │  ← .env file (gitignored)
│   (.env)             │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   python-dotenv      │  ← Load at startup
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Handler Classes    │  ← Use credentials
│   (Gemini, AWS)      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   External APIs      │  ← Never log credentials
│   (AWS, Gemini)      │
└──────────────────────┘

Security Features:
✓ No hardcoded secrets
✓ Environment-based config
✓ .env in .gitignore
✓ Minimal IAM permissions
✓ No credential logging
```

## Extensibility Points

### Adding a New AWS Service
```python
# In aws_handler.py

def _handle_newservice(self, action: str, params: Dict) -> Dict:
    """Handle NewService operations"""
    newservice = self._get_client('newservice')
    
    if action == "list":
        response = newservice.list_something()
        return {
            "success": True,
            "data": response['Items'],
            "message": "Operation successful"
        }
    
    return {"success": False, "error": f"Action '{action}' not recognized"}
```

### Adding a New Command Type
```python
# In command_processor.py

def process_command(self, command: str):
    # ... existing code ...
    
    elif command.startswith('@'):  # New prefix
        self._execute_custom_command(command[1:])
```

### Adding New UI Elements
```python
# In homepage.py

def display_custom_box(console: Console, message: str):
    """Display custom formatted message"""
    text = Text()
    text.append("★ ", style="bold yellow")
    text.append(message, style="white")
    console.print(Panel(text, border_style="yellow"))
```

## Performance Considerations

### Lazy Loading
```python
# Clients created only when needed
self._clients = {}  # Empty dict

def _get_client(self, service_name):
    if service_name not in self._clients:
        self._clients[service_name] = boto3.client(service_name)
    return self._clients[service_name]
```

### Efficient History
```python
# File-based history (not in memory)
history = FileHistory('.terminal_history')
# Max entries to prevent file bloat
max_entries = 1000
```

### Timeouts
```python
# Shell commands timeout after 30s
subprocess.run(..., timeout=30)
```

## Technology Stack Visual

```
┌─────────────────────────────────────────┐
│         APPLICATION LAYER               │
│  ┌─────────────────────────────────┐   │
│  │  AI-Powered AWS Smart Terminal  │   │
│  │  (Python 3.8+)                  │   │
│  └─────────────────────────────────┘   │
└────────────┬────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
    ▼                 ▼
┌─────────┐      ┌─────────┐
│Terminal │      │   AI    │
│   UI    │      │  Layer  │
├─────────┤      ├─────────┤
│prompt_  │      │ Gemini  │
│toolkit  │      │   API   │
│         │      │         │
│  rich   │      │ google- │
│ library │      │generati-│
│         │      │  veai   │
└────┬────┘      └────┬────┘
     │                │
     └────────┬───────┘
              │
              ▼
       ┌──────────────┐
       │   AWS SDK    │
       ├──────────────┤
       │    boto3     │
       │  (AWS APIs)  │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │  AWS Cloud   │
       │   Services   │
       └──────────────┘
```

---

**This architecture provides:**
- ✅ Clear separation of concerns
- ✅ Easy extensibility
- ✅ Maintainable code structure
- ✅ Robust error handling
- ✅ Security best practices
- ✅ Performance optimization
