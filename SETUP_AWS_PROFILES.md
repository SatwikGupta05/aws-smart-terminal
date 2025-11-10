# AWS Smart Terminal - Setup Guide
# Follow these steps to configure authentication using AWS profiles

## Step 1: Configure AWS Profiles

### For IAM User Mode (Recommended):
```powershell
aws configure --profile iam-user
```
When prompted, enter:
- AWS Access Key ID: YOUR_IAM_ACCESS_KEY
- AWS Secret Access Key: YOUR_IAM_SECRET_KEY
- Default region: us-east-1 (or your preferred region)
- Default output format: json

### For Root Account Mode (Not Recommended):
```powershell
aws configure --profile root-account
```
When prompted, enter:
- AWS Access Key ID: YOUR_ROOT_ACCESS_KEY
- AWS Secret Access Key: YOUR_ROOT_SECRET_KEY
- Default region: us-east-1
- Default output format: json

## Step 2: Configure config.ini

1. Copy this file: `config.ini.example` → `config.ini`
2. Edit `config.ini`:
   - Set your Gemini API key under [GEMINI] section
   - Choose your mode: demo, iam, or root
   - Verify profile names match what you configured above

## Step 3: Verify Setup

### Check AWS profiles:
```powershell
# List configured profiles
aws configure list-profiles

# Test IAM profile
aws sts get-caller-identity --profile iam-user

# Test Root profile (if configured)
aws sts get-caller-identity --profile root-account
```

### Check credential manager:
```powershell
python credential_manager.py
```

## Step 4: Switch Modes

```powershell
# Switch to demo mode (no AWS execution)
python switch_mode.py demo

# Switch to IAM mode (recommended)
python switch_mode.py iam

# Switch to root mode (not recommended)
python switch_mode.py root

# Check current mode
python switch_mode.py status
```

## Step 5: Run Terminal

```powershell
python main.py
```

## File Locations

### AWS Credentials (managed by AWS CLI):
- Windows: `C:\Users\YourName\.aws\credentials`
- Linux/Mac: `~/.aws/credentials`

### AWS Config (managed by AWS CLI):
- Windows: `C:\Users\YourName\.aws\config`
- Linux/Mac: `~/.aws/config`

### Project Config (your project):
- `config.ini` - Mode selection and Gemini key (in your project folder)

## Security Notes

✅ AWS credentials stored in `~/.aws/` (outside project, more secure)
✅ `config.ini` only has mode selection and Gemini key
✅ No `.env` file needed!
✅ Easy to switch between multiple AWS accounts
✅ Standard AWS CLI practice

## Troubleshooting

### "Profile not found" error:
```powershell
# List available profiles
aws configure list-profiles

# If profile missing, configure it:
aws configure --profile iam-user
```

### "Invalid credentials" error:
```powershell
# Test credentials
aws sts get-caller-identity --profile iam-user

# If expired, reconfigure:
aws configure --profile iam-user
```

### "Gemini API key not configured" error:
- Edit `config.ini`
- Replace `your_gemini_api_key_here` with actual key
- Get key from: https://makersuite.google.com/app/apikey

## Demo Mode (No AWS Account Needed)

If you just want to try the terminal without AWS:
1. Set `mode = demo` in `config.ini`
2. Add Gemini API key
3. Run `python main.py`
4. Commands will be previewed but not executed!

No AWS profile configuration needed for demo mode.
