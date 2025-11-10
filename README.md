# 🚀 AI-Powered AWS Smart Terminal

<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║     █████╗ ██╗    ██╗███████╗    ████████╗███████╗██████╗   ║
║    ██╔══██╗██║    ██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗  ║
║    ███████║██║ █╗ ██║███████╗       ██║   █████╗  ██████╔╝  ║
║    ██╔══██║██║███╗██║╚════██║       ██║   ██╔══╝  ██╔══██╗  ║
║    ██║  ██║╚███╔███╔╝███████║       ██║   ███████╗██║  ██║  ║
║    ╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝  ║
║            🤖 AI-Powered Smart Terminal v2.0 ☁️              ║
╚═══════════════════════════════════════════════════════════════╝
```

**An intelligent terminal that converts natural language into AWS CLI commands using Google's Gemini AI. Type what you want in plain English, AI generates the exact AWS CLI command, you confirm, and it executes!**

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![AWS CLI](https://img.shields.io/badge/AWS-CLI-orange.svg)](https://aws.amazon.com/cli/)
[![Gemini](https://img.shields.io/badge/AI-Gemini_2.0_Flash-purple.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Features](#-features) • [Installation](#%EF%B8%8F-installation) • [Usage](#-usage) • [Security](#-security) • [Documentation](#-documentation)

</div>

---

## ✨ Features

### 🤖 **Natural Language to AWS CLI**
- **Type in Plain English**: "list all my S3 buckets" → `aws s3 ls`
- **AI Translation**: Gemini AI converts your intent to exact AWS CLI commands
- **Confirmation Before Execution**: Review the command before it runs
- **Smart Context**: AI understands AWS service names, operations, and parameters

### ☁️ **Complete AWS CLI Integration**
- **All AWS Services**: EC2, S3, Lambda, RDS, DynamoDB, CloudFormation, and 200+ more
- **Direct Execution**: Commands run via AWS CLI (no boto3 wrapper)
- **Real-time Feedback**: See command output immediately
- **Error Handling**: Clear error messages and suggestions

### 🎮 **Three Operating Modes**
1. **Demo Mode** 🎯 - Try without AWS account (AI shows commands only)
2. **IAM User Mode** 🔒 - Safe, recommended for production
3. **Root Mode** ⚠️ - Full access (not recommended)

### 🔐 **Enhanced Security**
- **AWS Profiles**: Credentials stored in `~/.aws/credentials` (AWS CLI standard)
- **Config File**: Simple `config.ini` for mode selection and API keys
- **No .env Files**: No risk of committing AWS credentials
- **Git-Safe**: All sensitive files in `.gitignore`
- **Easy Mode Switching**: Switch between demo/iam/root with one command

### 🎨 **Beautiful Terminal Experience**
- **Rich Formatting**: Color-coded output with syntax highlighting
- **Command History**: Arrow key navigation (↑/↓)
- **Persistent History**: Saved between sessions
- **Retro ASCII Art**: Pixel art homepage and UI elements
- **Clear Status**: Always shows authentication mode and region

### �️ **Developer-Friendly**
- **Shell Commands**: Prefix with `!` to run any system command
- **Help System**: Prefix with `?` to ask AI questions
- **Extensible**: Easy to customize and extend
- **Well-Documented**: Comprehensive guides in `/Documentation`

---

## 🛠️ Installation

### Prerequisites

- **Python 3.13+** (3.8+ works, but 3.13+ recommended)
- **AWS CLI installed** ([Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))
- **Google Gemini API Key** ([Get it free](https://makersuite.google.com/app/apikey))
- **AWS Account** (optional for Demo Mode)

### Step 1: Clone & Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd "aws-smart-terminal"

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Step 2: Install AWS CLI

**Windows (PowerShell):**
```powershell
# Download and install
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi

# Verify installation
aws --version
```

**Linux:**
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

**macOS:**
```bash
brew install awscli
aws --version
```

### Step 3: Configure Authentication

#### Option A: Demo Mode (No AWS Account) 🎮

Perfect for learning and testing!

```bash
# Copy config template
copy config.ini.example config.ini

# Edit config.ini and set:
# mode = demo
# api_key = your_gemini_api_key_here
```

**What you get:**
- AI generates AWS CLI commands
- No actual AWS execution
- Perfect for learning AWS CLI syntax
- See what commands would be run

---

#### Option B: IAM User (Recommended) 🔒

Secure and production-ready.

1. **Configure AWS Profile:**
   ```bash
   aws configure --profile iam-user
   ```
   When prompted:
   - AWS Access Key ID: YOUR_IAM_ACCESS_KEY
   - AWS Secret Access Key: YOUR_IAM_SECRET_KEY
   - Default region: us-east-1
   - Default output format: json

2. **Configure `config.ini`:**
   ```bash
   copy config.ini.example config.ini
   ```
   Edit `config.ini`:
   ```ini
   [AUTH]
   mode = iam
   iam_profile = iam-user
   
   [GEMINI]
   api_key = your_gemini_api_key_here
   ```

3. **Switch to IAM mode:**
   ```bash
   python switch_mode.py iam
   ```

---

#### Option C: Root Account ⚠️

**Not recommended for production!**

Same as IAM but configure root profile:
```bash
aws configure --profile root-account
python switch_mode.py root
```

### Step 4: Run the Terminal

```bash
python main.py
```

You should see:
```
╔═══════════════════════════════════════════════════════════════╗
║                  🤖 AI-Powered Smart Terminal ☁️             ║
╚═══════════════════════════════════════════════════════════════╝

🔐 Authentication: IAM User
🌍 Region: us-east-1
💎 AI Model: gemini-2.0-flash-exp

Type 'home' for main menu, '?' for help, 'exit' to quit
>
```

---

## 🎯 Usage

### Natural Language Commands

The magic of this terminal is **natural language understanding**. Just type what you want!

#### Example Commands:

**S3 Operations:**
```
> list all my S3 buckets
> create a bucket named my-data-bucket
> upload file.txt to my-bucket
> delete bucket old-bucket
```

**EC2 Operations:**
```
> list all running EC2 instances
> start instance i-1234567890abcdef0
> stop all instances tagged environment=dev
> create an EC2 instance with t2.micro
```

**Lambda Functions:**
```
> list all lambda functions
> invoke function my-function with test data
> show logs for my-function
```

**RDS Databases:**
```
> list all RDS instances
> create a MySQL database
> stop database my-db-instance
```

**Multi-Service:**
```
> show me all resources in us-west-2
> list everything I'm paying for
> what's running in my account
```

### Command Flow

1. **Type in natural language:**
   ```
   > list all my S3 buckets
   ```

2. **AI generates AWS CLI command:**
   ```
   💡 Generated Command:
   aws s3 ls
   
   📝 Description: Lists all S3 buckets in your account
   ```

3. **You confirm:**
   ```
   Execute this command? [Y/n]: y
   ```

4. **See results immediately:**
   ```
   ✅ Command executed successfully!
   
   2024-01-15 12:30:45 my-first-bucket
   2024-02-20 09:15:30 data-backup-bucket
   2024-03-10 14:22:18 website-assets
   ```

### Special Prefixes

#### Shell Commands (`!` prefix)
Run any system command:
```
> !dir                    # List directory contents
> !cd Documents          # Change directory
> !python --version      # Check Python version
> !git status           # Git commands
> !aws s3 ls            # Direct AWS CLI (bypasses AI)
```

#### Help Mode (`?` prefix)
Ask the AI questions:
```
> ?how do I create an S3 bucket
> ?what are EC2 instance types
> ?explain lambda functions
> ?difference between IAM role and IAM user
```

### Built-in Commands

| Command | Description |
|---------|-------------|
| `home` or `homepage` | Display ASCII art homepage |
| `clear` | Clear the terminal screen |
| `history` | Show command history |
| `exit` or `quit` | Exit the terminal |
| `help` | Show available commands |

### Demo Mode Usage

When `mode = demo` in your `config.ini`:

```
> create an EC2 instance with t2.micro

🎮 DEMO MODE - Command Preview Only

💡 Generated AWS CLI Command:
aws ec2 run-instances --image-id ami-0abcdef1234567890 \
    --instance-type t2.micro --count 1

📝 What this does:
Launches a new EC2 instance with t2.micro instance type

⚠️  This command was NOT executed (Demo Mode active)
To execute real commands, configure AWS credentials and switch mode
```

---

## 🔐 Security

### 🔒 AWS Profiles Method

This project uses **AWS CLI standard profiles** for credential management:

**Benefits:**
- ✅ AWS credentials stored in `~/.aws/credentials` (outside project folder)
- ✅ Standard AWS CLI practice
- ✅ Works with all AWS tools
- ✅ No risk of committing credentials to Git
- ✅ Easy to manage multiple AWS accounts

### Configuration Files

**`config.ini`** (Your settings - gitignored):
```ini
[AUTH]
mode = iam  # or demo or root

[GEMINI]
api_key = your_gemini_api_key_here
```

**`~/.aws/credentials`** (AWS credentials - managed by AWS CLI):
```ini
[iam-user]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/...

[root-account]
aws_access_key_id = AKIAIOSFODNN7ROOT
aws_secret_access_key = wJalrXUtnFEMI/...
```

### Mode Switching

```bash
# Check current mode
python switch_mode.py status

# Switch to demo mode (no AWS execution)
python switch_mode.py demo

# Switch to IAM mode (safe AWS execution)
python switch_mode.py iam

# Switch to root mode (full AWS access)
python switch_mode.py root
```

### Best Practices

1. **Never Commit Credentials**
   - `config.ini` is in `.gitignore` - keeps your Gemini API key safe
   - AWS credentials in `~/.aws/` - never in project folder
   - Always verify before `git push`

2. **Use IAM Users, Not Root**
   - Create IAM users with minimal permissions
   - Enable MFA for IAM users
   - Root credentials should NEVER be used for daily operations

3. **Rotate Credentials Regularly**
   - Change AWS keys every 90 days
   - Rotate Gemini API key periodically
   - Delete old/unused keys

4. **Principle of Least Privilege**
   - Grant only necessary permissions
   - Use IAM policies to restrict actions
   - Avoid `AdministratorAccess` when possible

5. **Monitor AWS Usage**
   - Enable CloudTrail for audit logs
   - Set up billing alerts
   - Review IAM access regularly

6. **Secure Your Machine**
   - Use full-disk encryption
   - Lock your computer when away
   - Keep OS and Python updated

### What's Protected

**In `~/.aws/credentials` (AWS CLI):**
```ini
aws_access_key_id = AKIAIOSFODNN7EXAMPLE     # ← Protected (outside project)
aws_secret_access_key = wJalrXUtnFEMI...    # ← Protected (outside project)
```

**In `config.ini` (Your project):**
```ini
api_key = AIzaSyC_1234567890abcdef...      # ← Protected (gitignored)
```

---

## 📋 Requirements

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, Linux (Ubuntu 20.04+)
- **Python**: 3.13+ (tested), 3.8+ minimum
- **RAM**: 2GB minimum, 4GB recommended
- **Disk Space**: 500MB for dependencies

### Python Dependencies
```txt
google-generativeai>=0.8.3  # Gemini AI integration
prompt-toolkit>=3.0.52      # Terminal interface
rich>=14.2.0                # Beautiful terminal output
python-dotenv>=1.0.0        # Environment variables (legacy support)
```

Install all: `pip install -r requirements.txt`

### External Requirements
- **AWS CLI**: Must be installed separately ([guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))
- **Gemini API Key**: Free tier available ([get key](https://makersuite.google.com/app/apikey))
- **AWS Account**: Optional for demo mode, required for real execution
- **Internet**: Required for AI and AWS API calls

---

## 📁 Project Structure

```
aws-smart-terminal/
│
├── 📄 main.py                      # Entry point - Terminal loop
├── 📄 gemini_handler.py            # Gemini AI integration
├── 📄 aws_handler.py               # AWS CLI verification
├── 📄 command_processor.py         # Command parsing & execution
├── 📄 homepage.py                  # ASCII art homepage
├── 📄 credential_manager.py        # Credential loading from config.ini
├── 📄 switch_mode.py               # Mode switching utility
│
├── 📋 requirements.txt             # Python dependencies
├── 🔒 config.ini                   # Your configuration (gitignored)
├── 🔒 config.ini.example           # Configuration template
├── 🚫 .gitignore                   # Git ignore rules
├── 📖 README.md                    # This file
│
├── 📁 Documentation/               # Extended documentation
│   ├── PROJECT_GUIDE.md           # Complete project guide
│   ├── QUICKSTART_AWS_PROFILES.md # Quick start guide
│   ├── SETUP_AWS_PROFILES.md      # Detailed setup
│   ├── AWS_PROFILES_IMPLEMENTATION.md # Implementation details
│   ├── ARCHITECTURE.md            # System architecture
│   ├── AWS_INTEGRATION.md         # AWS CLI details
│   ├── COMMAND_EXAMPLES.md        # Example commands
│   └── ERROR_HANDLING.md          # Error troubleshooting
│
└── 🏠 ~/.aws/                      # AWS CLI configuration (system-level)
    ├── credentials                 # AWS access keys
    └── config                      # AWS settings
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **[PROJECT_GUIDE.md](Documentation/PROJECT_GUIDE.md)** | Complete project guide with demo script |
| **[AUTH_GUIDE.md](Documentation/AUTH_GUIDE.md)** | Detailed authentication setup |
| **[DEMO_MODE.md](Documentation/DEMO_MODE.md)** | Using demo mode without AWS |
| **[SETUP_AWS_PROFILES.md](SETUP_AWS_PROFILES.md)** | AWS Profiles setup guide |
| **[QUICKSTART_AWS_PROFILES.md](QUICKSTART_AWS_PROFILES.md)** | Quick start with AWS Profiles |
| **[AWS_PROFILES_IMPLEMENTATION.md](AWS_PROFILES_IMPLEMENTATION.md)** | Implementation details |
| **[ARCHITECTURE.md](Documentation/ARCHITECTURE.md)** | System design and architecture |
| **[AWS_INTEGRATION.md](Documentation/AWS_INTEGRATION.md)** | AWS CLI integration details |
| **[COMMAND_EXAMPLES.md](Documentation/COMMAND_EXAMPLES.md)** | 50+ example commands |
| **[ERROR_HANDLING.md](Documentation/ERROR_HANDLING.md)** | Troubleshooting guide |

---

## 🎨 Terminal Features

### Command History
- **↑/↓ Arrow Keys**: Browse previous commands
- **Ctrl+R**: Search command history
- **Persistent**: History saved in `~/.aws_terminal_history`

### Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel current command |
| `Ctrl+D` | Exit terminal |
| `Ctrl+L` | Clear screen (same as `clear`) |
| `Ctrl+R` | Reverse search history |
| `Tab` | Auto-complete (basic) |

### Output Formatting
- **Color Coding**: Success (green), errors (red), info (blue)
- **Syntax Highlighting**: AWS CLI commands highlighted
- **Tables**: Structured data in readable tables
- **Markdown Support**: Rich text rendering

### Exiting & Cleanup

**How to exit the terminal:**
```bash
# Method 1: Type exit command
> exit

# Method 2: Type quit command
> quit

# Method 3: Press keyboard shortcut
Ctrl+D
```

**Complete shutdown workflow:**
```bash
# Step 1: Exit the AWS terminal
> exit

# Step 2: Deactivate virtual environment
deactivate
```

**Why deactivate venv?**
- Returns to system Python
- Frees terminal for other projects
- Clean environment management
- Best practice for venv usage

---

## 🚀 Quick Start Examples

### First Time Setup
```bash
# 1. Install
git clone <repo-url>
cd "Cli terminal"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 2. Configure (Demo Mode)
copy config.ini.example config.ini
# Edit config.ini: Set mode=demo and add your GEMINI_API_KEY

# 3. Run
python main.py

# 4. Try it!
> list all my S3 buckets
> create an EC2 instance
> ?how do I use Lambda functions

# 5. Exit when done
> exit
# Or press Ctrl+D

# 6. Deactivate virtual environment
deactivate
```

### Real AWS Operations
```bash
# 1. Configure AWS credentials using AWS CLI
aws configure --profile iam-user
# Enter your AWS Access Key ID, Secret Access Key, region, and output format

# 2. Update config.ini to use IAM mode
python switch_mode.py iam
# This updates config.ini to: mode=iam, iam_profile=iam-user

# 3. Run
python main.py

# 4. Execute real commands
> list all my S3 buckets          # Actually lists your buckets!
> create bucket my-new-bucket    # Creates real bucket!

# 5. Exit the terminal
> exit
# Or press Ctrl+D

# 6. Deactivate virtual environment
deactivate
```

### Switching Between Modes

**Switch authentication modes easily:**

```bash
# Switch to Demo Mode (no real AWS operations)
python switch_mode.py demo

# Switch to IAM Mode (use IAM user credentials)
python switch_mode.py iam

# Switch to Root Mode (use root account credentials)
python switch_mode.py root

# Check current mode
python switch_mode.py
```

### Shutting Down Properly

**When you're done working:**

```bash
# Step 1: Exit the terminal
> exit
# Or press Ctrl+D

# Step 2: Deactivate virtual environment (Windows PowerShell)
deactivate
```

**Platform-specific deactivation:**
```bash
# Windows PowerShell/CMD:
deactivate

# Linux/Mac:
deactivate

# All platforms use the same command!
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Update documentation for new features
- Test in demo mode before real AWS
- Keep dependencies minimal

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `AWS CLI not found`
- **Fix**: Install AWS CLI from [official guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- **Verify**: Run `aws --version` in terminal

**Issue**: `Invalid Gemini API key`
- **Fix**: Get new key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Check**: Ensure no spaces in `config.ini` file

**Issue**: `Permission denied` errors in AWS
- **Fix**: Check IAM user permissions
- **Verify**: User has necessary AWS service permissions

**Issue**: Commands execute but show errors
- **Fix**: Check AWS CLI is configured: `aws configure list`
- **Verify**: Region and credentials are correct

For more help, see [`Documentation/ERROR_HANDLING.md`](Documentation/ERROR_HANDLING.md)

---

## 📊 Supported AWS Services

This terminal supports **ALL AWS CLI commands** across 200+ services:

### Popular Services
- **Compute**: EC2, Lambda, ECS, EKS, Fargate
- **Storage**: S3, EBS, EFS, Glacier
- **Database**: RDS, DynamoDB, Aurora, ElastiCache
- **Networking**: VPC, Route53, CloudFront, ELB
- **Security**: IAM, KMS, Secrets Manager, WAF
- **Monitoring**: CloudWatch, CloudTrail, X-Ray
- **AI/ML**: SageMaker, Rekognition, Comprehend
- **Analytics**: Athena, EMR, Kinesis, QuickSight
- **Developer**: CodeCommit, CodeBuild, CodeDeploy
- **Containers**: ECS, EKS, ECR, App Runner

Any valid AWS CLI command works!

---

## ⚡ Performance Tips

1. **Use specific commands** - "list S3 buckets" vs "show everything"
2. **Region awareness** - Specify region to avoid cross-region calls
3. **Demo mode for testing** - Test commands before real execution
4. **Batch operations** - Group similar commands together
5. **Command history** - Reuse successful commands with ↑

---

## 📄 License

MIT License - Free for personal and commercial use.

See [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google Gemini AI** - Natural language understanding and command generation
- **AWS** - Cloud infrastructure and comprehensive CLI
- **prompt_toolkit** - Beautiful terminal interface library
- **Rich** - Terminal formatting and styling
- **Python Community** - Amazing ecosystem and libraries

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

## 📬 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/repo/discussions)
- **Email**: your.email@example.com

---

## � Roadmap

### Planned Features
- [ ] Multi-region command execution
- [ ] Command templates and aliases
- [ ] AWS cost estimation before execution
- [ ] Command scheduling and automation
- [ ] Integration with AWS SSO
- [ ] Web UI for remote access
- [ ] Plugin system for custom commands
- [ ] Command validation and dry-run mode

### Version History
- **v2.0** (Current) - AWS CLI direct execution, password protection
- **v1.0** - Initial release with boto3 integration

---

<div align="center">

### Built with ❤️ by developers, for developers

**[⬆ Back to Top](#-ai-powered-aws-smart-terminal)**

---

[![Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python&logoColor=white)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/Powered%20by-AWS-orange?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![AI](https://img.shields.io/badge/AI-Gemini-purple?logo=google&logoColor=white)](https://ai.google.dev/)

**Type what you want. AI does the rest. ✨**

</div>
