# 📚 Command Reference Guide

## Natural Language Commands

### S3 Operations

#### List Operations
```
list all S3 buckets
show me all S3 buckets
what S3 buckets do I have
display my S3 buckets

list files in bucket my-bucket
show objects in my-bucket
what's in my S3 bucket called my-bucket
```

#### Create/Upload Operations
```
create an S3 bucket called my-new-bucket
make a new S3 bucket named test-bucket

upload file.txt to my-bucket
upload data.csv to bucket my-data-bucket
put myfile.pdf in my-bucket
```

#### Download Operations
```
download myfile.txt from my-bucket
get data.csv from bucket my-bucket
```

#### Delete Operations
```
delete S3 bucket my-old-bucket
remove bucket test-bucket
```

---

### EC2 Operations

#### List Operations
```
list all EC2 instances
show me my EC2 instances
what EC2 instances are running
display all my virtual machines
```

#### Create/Launch Operations
```
create an EC2 instance
launch a new EC2 instance
start a t2.micro EC2 instance
create an EC2 instance with t2.small
launch a new virtual machine with t2.medium
```

#### Control Operations
```
stop EC2 instance i-1234567890abcdef0
start instance i-1234567890abcdef0
terminate EC2 instance i-1234567890abcdef0
```

---

### Lambda Operations

#### List Operations
```
list all Lambda functions
show me my Lambda functions
what Lambda functions do I have
display all my serverless functions
```

#### Invoke Operations
```
invoke Lambda function my-function
run Lambda function data-processor
execute my-lambda-function
```

---

### RDS Operations

#### List Operations
```
list all RDS instances
show me my RDS databases
what databases do I have
display my RDS instances
```

---

### IAM Operations

#### List Operations
```
list all IAM users
show me IAM users
who are the IAM users
display all users
```

---

### DynamoDB Operations

#### List Operations
```
list all DynamoDB tables
show me my DynamoDB tables
what DynamoDB tables exist
display all NoSQL tables
```

---

### CloudWatch Operations

#### List Operations
```
list CloudWatch metrics
show me CloudWatch metrics
what metrics are available
```

---

### SNS Operations

#### List Operations
```
list all SNS topics
show me SNS topics
what SNS topics exist
```

---

### SQS Operations

#### List Operations
```
list all SQS queues
show me SQS queues
what queues do I have
```

---

## Shell Commands (! prefix)

### Windows PowerShell Commands
```
!dir                          # List files in current directory
!cd path\to\folder           # Change directory
!pwd                          # Print working directory
!echo Hello                   # Print text
!type file.txt               # Display file contents
!copy file.txt backup.txt    # Copy file
!move file.txt newlocation\  # Move file
!del file.txt                # Delete file
!mkdir newfolder             # Create directory
!rmdir oldfolder             # Remove directory
!python --version            # Check Python version
!pip list                    # List installed packages
!git status                  # Check git status
!git log --oneline -5        # Show recent commits
!aws --version               # Check AWS CLI version
!ipconfig                    # Network configuration
!systeminfo                  # System information
!Get-Process                 # List running processes
!Get-Service                 # List services
```

### Common Cross-Platform Commands
```
!python script.py            # Run Python script
!pip install package         # Install Python package
!npm install                 # Install Node.js packages
!docker ps                   # List Docker containers
!kubectl get pods            # List Kubernetes pods
```

---

## Help Commands (? prefix)

### AWS Service Questions
```
?what is S3
?how does S3 work
?what is EC2
?explain EC2 instance types
?what is Lambda
?how do Lambda functions work
?what is RDS
?what databases does RDS support
?what is IAM
?explain IAM roles vs users
```

### How-To Questions
```
?how do I create an S3 bucket
?how to upload files to S3
?how do I launch an EC2 instance
?how to stop an EC2 instance
?how do I create a Lambda function
?how to invoke a Lambda function
?how do I set up RDS
?how to create IAM users
```

### Best Practices
```
?S3 security best practices
?EC2 cost optimization
?Lambda performance tips
?RDS backup strategies
?IAM security recommendations
?how to secure my AWS account
```

### Troubleshooting
```
?why can't I access my S3 bucket
?EC2 instance won't start
?Lambda function timeout error
?RDS connection issues
?IAM permission denied error
```

### Cost & Pricing
```
?how much does S3 cost
?EC2 pricing
?Lambda pricing model
?RDS pricing
?how to reduce AWS costs
```

---

## Special Commands

### Terminal Control
```
exit                    # Exit the terminal
quit                    # Exit the terminal
bye                     # Exit the terminal

clear                   # Clear the screen
cls                     # Clear the screen (Windows)
```

### Information & Navigation
```
home                    # Show homepage
homepage                # Show homepage

history                 # Display command history
```

---

## Advanced Examples

### Multi-Step Operations
```
# First create a bucket
create an S3 bucket called my-data-bucket

# Then upload a file
upload mydata.csv to my-data-bucket

# List contents to verify
list objects in my-data-bucket
```

### Combined with Shell Commands
```
# Check local file first
!dir *.csv

# Upload it
upload data.csv to my-bucket

# Verify on AWS
list files in my-bucket
```

### Using Help for Guidance
```
# Learn about a service
?what is EC2 and when should I use it

# Then use it
create an EC2 instance with t2.micro
```

---

## Tips & Tricks

### Natural Language Tips
1. Be specific but natural - "list all S3 buckets" or "show my S3 buckets" both work
2. Service names can be uppercase or lowercase - "S3" or "s3" are the same
3. You can use synonyms - "virtual machines" for "EC2 instances"
4. Bucket/instance names should be exact

### Shell Command Tips
1. Always prefix with `!` for shell commands
2. Remember you're in PowerShell on Windows
3. Use quotes for paths with spaces: `!cd "My Documents"`
4. Commands run in the current terminal context

### Help Query Tips
1. Start with `?` for any question
2. Ask in plain English
3. Be as specific as possible
4. Include service names when relevant

### Command History Tips
1. Press ↑ to recall previous command
2. Press ↓ to move forward in history
3. Edit recalled commands before executing
4. History persists between sessions

---

## Error Messages & Solutions

### "AWS credentials not found"
**Solution**: Check your `.env` file has correct `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

### "GEMINI_API_KEY not found"
**Solution**: Add your Gemini API key to `.env` file

### "Bucket name required"
**Solution**: Be more specific in your command, include the bucket name

### "Service not yet supported"
**Solution**: The AWS service you're trying to use isn't implemented yet

### "Permission denied"
**Solution**: Your IAM user needs additional permissions for this operation

---

## Examples by Use Case

### Setting Up a New Project
```
# Create S3 bucket for storage
create an S3 bucket called project-data-bucket

# Launch EC2 instance for application
create an EC2 instance with t2.micro

# Check what's running
list all EC2 instances
```

### Data Management
```
# Upload local files
!dir *.csv
upload data-2024.csv to my-data-bucket

# Check upload
list files in my-data-bucket

# Download when needed
download processed-data.csv from my-data-bucket
```

### Monitoring & Maintenance
```
# Check running instances
list all EC2 instances

# Check Lambda functions
list all Lambda functions

# Check databases
list all RDS instances

# View metrics
list CloudWatch metrics
```

---

## Quick Reference Card

| Command Type | Prefix | Example |
|--------------|--------|---------|
| AWS Natural Language | (none) | `list all S3 buckets` |
| Shell Command | `!` | `!dir` |
| Help/Question | `?` | `?what is S3` |
| Exit | (none) | `exit` |
| Clear Screen | (none) | `clear` |
| Show History | (none) | `history` |
| Show Homepage | (none) | `home` |

---

**Remember**: This terminal is designed to understand natural language, so feel free to phrase commands in your own words! The AI will interpret your intent.
