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
- **Password-Protected Credentials**: Encrypt `.env` file with `secure_env.py`
- **No Hardcoded Secrets**: Environment-based configuration
- **Git-Safe**: All sensitive files in `.gitignore`
- **Strong Encryption**: PBKDF2 + AES-128 via Fernet

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
# Copy example config
copy .env.example .env

# Edit .env file and set:
AWS_AUTH_METHOD=demo
GEMINI_API_KEY=your_gemini_api_key_here
```

**What you get:**
- AI generates AWS CLI commands
- No actual AWS execution
- Perfect for learning AWS CLI syntax
- See what commands would be run

---

#### Option B: IAM User (Recommended) 🔒

Secure and production-ready.

1. **Create IAM User in AWS Console:**
   - Go to IAM → Users → Create User
   - Enable "Programmatic access"
   - Attach policies (e.g., PowerUserAccess)
   - Save Access Key ID & Secret Access Key

2. **Configure `.env`:**
   ```env
   AWS_AUTH_METHOD=iam
   AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
   AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   AWS_DEFAULT_REGION=us-east-1
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Secure your credentials** (optional but recommended):
   ```bash
   python secure_env.py
   # Choose option 1 to lock .env with password
   ```

---

#### Option C: Root Account ⚠️

**Not recommended for production!**

Same as IAM but use root account credentials:
```env
AWS_AUTH_METHOD=root
ROOT_ACCESS_KEY_ID=your_root_access_key
ROOT_SECRET_ACCESS_KEY=your_root_secret_key
AWS_DEFAULT_REGION=us-east-1
GEMINI_API_KEY=your_gemini_api_key_here
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

When `AWS_AUTH_METHOD=demo` in your `.env`:

```
> create an EC2 instance with t2.micro

🎮 DEMO MODE - Command Preview Only

💡 Generated AWS CLI Command:
aws ec2 run-instances --image-id ami-0abcdef1234567890 \
    --instance-type t2.micro --count 1

📝 What this does:
Launches a new EC2 instance with t2.micro instance type

⚠️  This command was NOT executed (Demo Mode active)
To execute real commands, configure AWS credentials in .env
```

---

## 🔐 Security

### 🔒 Password-Protected Credentials

**New Feature!** Encrypt your `.env` file with a password:

```bash
# Encrypt .env file
python secure_env.py
# Choose option 1: Lock .env file
# Enter strong password (min 8 chars)
# Creates: .env.encrypted and .env.salt
# Deletes: .env (plaintext removed)

# When you need to use the terminal
python secure_env.py
# Choose option 1: Unlock .env file
# Enter password
# Restores: .env file

# Run your terminal
python main.py

# Lock it again when done
python secure_env.py
```

**Security Features:**
- ✅ PBKDF2 key derivation (100,000 iterations)
- ✅ AES-128 encryption via Fernet
- ✅ No password storage
- ✅ Unique salt per encryption
- ✅ Git-safe (encrypted files in `.gitignore`)

📖 **Full guide:** [`Documentation/SECURE_ENV.md`](Documentation/SECURE_ENV.md)

### Best Practices

1. **Never Commit Credentials**
   - `.env` is in `.gitignore` - keep it there!
   - Use `.env.example` as template
   - Always verify before `git push`

2. **Use IAM Users, Not Root**
   - Create IAM users with minimal permissions
   - Enable MFA for IAM users
   - Root credentials should NEVER be in `.env`

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

### What's Protected in `.env`

```env
# These are encrypted when you lock .env:
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE          # ← Protected
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI...          # ← Protected
ROOT_ACCESS_KEY_ID=AKIAIOSFODNN7ROOT           # ← Protected
ROOT_SECRET_ACCESS_KEY=wJalrXUtnFEMI...        # ← Protected
GEMINI_API_KEY=AIzaSyC_1234567890abcdef...     # ← Protected
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
python-dotenv>=1.0.0        # Environment variables
cryptography>=41.0.0        # Credential encryption
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
Cli terminal/
│
├── 📄 main.py                      # Entry point - Terminal loop
├── 📄 gemini_handler.py            # Gemini AI integration
├── 📄 aws_handler.py               # AWS CLI verification
├── 📄 command_processor.py         # Command parsing & execution
├── 📄 homepage.py                  # ASCII art homepage
├── 📄 secure_env.py                # Credential encryption utility
│
├── 📋 requirements.txt             # Python dependencies
├── 🔒 .env.example                 # Configuration template
├── 🚫 .gitignore                   # Git ignore rules
├── 📖 README.md                    # This file
│
└── 📁 Documentation/               # Extended documentation
    ├── AUTH_GUIDE.md              # Authentication setup
    ├── DEMO_MODE.md               # Demo mode guide
    ├── SECURE_ENV.md              # Encryption guide
    ├── PROJECT_GUIDE.md           # Complete project guide
    ├── ARCHITECTURE.md            # System architecture
    ├── AWS_INTEGRATION.md         # AWS CLI details
    ├── COMMAND_EXAMPLES.md        # Example commands
    ├── ERROR_HANDLING.md          # Error troubleshooting
    ├── PIXEL_ART_EXAMPLES.md      # ASCII art examples
    └── examples.py                # Code examples
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **[PROJECT_GUIDE.md](Documentation/PROJECT_GUIDE.md)** | Complete project guide with demo script |
| **[AUTH_GUIDE.md](Documentation/AUTH_GUIDE.md)** | Detailed authentication setup |
| **[DEMO_MODE.md](Documentation/DEMO_MODE.md)** | Using demo mode without AWS |
| **[SECURE_ENV.md](Documentation/SECURE_ENV.md)** | Password-protect your credentials |
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

# Step 3: Lock credentials (recommended before closing)
python secure_env.py
# Choose option 1 to lock .env
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
copy .env.example .env
# Edit .env: Set AWS_AUTH_METHOD=demo and add GEMINI_API_KEY

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
# 1. Configure AWS credentials in .env
# Set AWS_AUTH_METHOD=iam
# Add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY

# 2. Run
python main.py

# 3. Execute real commands
> list all my S3 buckets          # Actually lists your buckets!
> create bucket my-new-bucket    # Creates real bucket!

# 4. Exit the terminal
> exit
# Or press Ctrl+D

# 5. Deactivate virtual environment
deactivate
```

### Shutting Down Properly

**When you're done working:**

```bash
# Step 1: Exit the terminal
> exit
# Or press Ctrl+D

# Step 2: Deactivate virtual environment (Windows PowerShell)
deactivate

# Step 3: Lock your credentials (optional but recommended)
python secure_env.py
# Choose option 1 to lock .env
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

**Issue**: `ImportError: cannot import name 'PBKDF2'`
- **Fix**: Change `PBKDF2` to `PBKDF2HMAC` in `secure_env.py`

**Issue**: `AWS CLI not found`
- **Fix**: Install AWS CLI from [official guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- **Verify**: Run `aws --version` in terminal

**Issue**: `Invalid Gemini API key`
- **Fix**: Get new key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Check**: Ensure no spaces in `.env` file

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
