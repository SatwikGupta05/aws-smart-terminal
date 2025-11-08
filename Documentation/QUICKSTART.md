# 🚀 Quick Start Guide

## Setup Instructions

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project directory:
```powershell
copy .env.example .env
```

Edit `.env` and add your credentials:

**Option A: Using IAM User (RECOMMENDED) ✅**
```
AWS_AUTH_METHOD=iam
AWS_ACCESS_KEY_ID=your_iam_access_key
AWS_SECRET_ACCESS_KEY=your_iam_secret_key
AWS_DEFAULT_REGION=us-east-1
GEMINI_API_KEY=your_actual_gemini_api_key
```

**Option B: Using Root Account (NOT RECOMMENDED) ⚠️**
```
AWS_AUTH_METHOD=root
AWS_ROOT_ACCESS_KEY_ID=your_root_access_key
AWS_ROOT_SECRET_ACCESS_KEY=your_root_secret_key
AWS_DEFAULT_REGION=us-east-1
GEMINI_API_KEY=your_actual_gemini_api_key
```

**💡 Tip:** You can keep both sets of credentials and switch by changing `AWS_AUTH_METHOD`

For detailed authentication setup, see [AUTH_GUIDE.md](AUTH_GUIDE.md)

#### Getting AWS Credentials
1. Log in to AWS Console
2. Navigate to IAM → Users → Your User → Security Credentials
3. Create Access Key
4. Copy Access Key ID and Secret Access Key

#### Getting Gemini API Key
1. Visit https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

### 3. Run the Terminal
```powershell
python main.py
```

## Example Commands

### Natural Language (Direct Input)
```
> list all my S3 buckets
> show me all EC2 instances
> create an S3 bucket called my-test-bucket
> list all Lambda functions
> describe my RDS instances
```

### Shell Commands (! prefix)
```
> !dir
> !cd ..
> !python --version
> !git status
> !echo Hello World
```

### Help/Questions (? prefix)
```
> ?how do I create an S3 bucket
> ?what is EC2
> ?explain Lambda pricing
> ?best practices for S3 security
```

### Special Commands
```
> home          # Show homepage
> history       # View command history
> clear         # Clear screen
> exit          # Exit terminal
```

## Troubleshooting

### Import Errors
If you see import errors, make sure all dependencies are installed:
```powershell
pip install --upgrade -r requirements.txt
```

### AWS Credentials Error
- Check that your `.env` file exists and has correct credentials
- Verify credentials work using AWS CLI: `aws sts get-caller-identity`
- Ensure IAM user has appropriate permissions

### Gemini API Error
- Verify your API key is valid
- Check you haven't exceeded API quota
- Visit Google AI Studio to check API status

## Next Steps

1. **Test AWS Connection**: Try `list all S3 buckets`
2. **Test AI Help**: Try `?what is EC2`
3. **Test Shell Commands**: Try `!dir`
4. **Explore**: Type natural language commands!

## Security Notes

⚠️ **IMPORTANT**:
- Never commit your `.env` file to version control
- Use IAM roles with minimal required permissions
- Rotate credentials regularly
- Consider using AWS SSO for production

## Features Implemented

✅ Natural Language Processing with Gemini AI
✅ Full AWS Integration (EC2, S3, Lambda, RDS, IAM, CloudWatch, DynamoDB, SNS, SQS)
✅ Command History with Arrow Key Navigation
✅ Persistent History Between Sessions
✅ Shell Command Execution (! prefix)
✅ AI Help System (? prefix)
✅ Colorful Terminal Output
✅ Pixel Art Homepage
✅ Error Handling & User Feedback

## Advanced Usage

### Custom AWS Region
Change the region in `.env`:
```
AWS_DEFAULT_REGION=eu-west-1
```

### History File Location
Customize history file location in `.env`:
```
HISTORY_FILE=.my_custom_history
MAX_HISTORY_ENTRIES=5000
```

Enjoy your AI-Powered AWS Smart Terminal! 🎉
