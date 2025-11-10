# 🚀 Quick Start Guide - AWS Profiles Method

## Overview
This project uses **AWS profiles** (standard AWS CLI method) instead of `.env` files to manage credentials.

✅ **AWS credentials** → Stored in `~/.aws/credentials` (encrypted by AWS CLI)
✅ **Mode selection** → Stored in `config.ini` (safe to share)
✅ **Gemini API key** → Stored in `config.ini` (gitignored)

---

## 📋 Initial Setup (5 minutes)

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Create Config File
```powershell
copy config.ini.example config.ini
```

### 3. Add Gemini API Key
Edit `config.ini` and add your Gemini API key:
```ini
[GEMINI]
api_key = AIzaSyC_your_actual_key_here
```
Get key from: https://makersuite.google.com/app/apikey

---

## 🎮 Demo Mode (No AWS Account Needed!)

**Perfect for learning, testing, and practicing AWS CLI commands**

### Setup:
```powershell
# config.ini is already set to demo mode by default
python switch_mode.py demo
```

### Run:
```powershell
python main.py
```

### What You Get:
- ✅ AI generates AWS CLI commands
- ✅ Commands are shown but NOT executed
- ✅ Learn AWS CLI syntax
- ❌ No AWS account required
- ❌ No AWS credentials needed

---

## 🔒 IAM Mode (Recommended for Real AWS)

**Safe, production-ready AWS execution with limited permissions**

### Setup:
```powershell
# 1. Configure AWS IAM profile
aws configure --profile iam-user
# Enter: Access Key, Secret Key, Region, Format

# 2. Switch to IAM mode
python switch_mode.py iam
```

### Verify:
```powershell
aws sts get-caller-identity --profile iam-user
```

### Run:
```powershell
python main.py
```

### What You Get:
- ✅ Real AWS command execution
- ✅ Limited permissions (based on IAM policy)
- ✅ Safer than root account
- ✅ Credentials in `~/.aws/` (outside project)

---

## ⚠️ Root Mode (NOT Recommended)

**Full AWS access - use only for testing/personal accounts**

### Setup:
```powershell
# 1. Configure AWS root profile
aws configure --profile root-account
# Enter: Root Access Key, Secret Key, Region, Format

# 2. Switch to root mode
python switch_mode.py root
```

### Run:
```powershell
python main.py
```

### What You Get:
- ✅ Real AWS command execution
- ⚠️ FULL access to all AWS services
- ⚠️ No permission restrictions
- ⚠️ Use at your own risk!

---

## 🔄 Switching Between Modes

```powershell
# Check current mode
python switch_mode.py status

# Switch to demo (no AWS execution)
python switch_mode.py demo

# Switch to IAM (safe AWS execution)
python switch_mode.py iam

# Switch to root (full AWS access)
python switch_mode.py root
```

**No need to restart the terminal! Just switch and run `python main.py` again.**

---

## 📁 File Structure

```
Your Project:
├── config.ini           # Your settings (gitignored - has Gemini key)
├── config.ini.example   # Template (safe to commit)
├── credential_manager.py # Loads credentials
├── switch_mode.py       # Mode switcher utility
└── main.py              # Terminal application

System Files:
└── C:\Users\YourName\.aws\
    ├── credentials      # AWS keys (managed by AWS CLI)
    └── config          # AWS settings (regions, etc.)
```

---

## 🎯 Common Workflows

### Learning AWS (No Account):
```powershell
python switch_mode.py demo
python main.py
> list all S3 buckets
# Shows: aws s3 ls (not executed)
```

### Daily Work (IAM):
```powershell
python switch_mode.py iam
python main.py
> list all S3 buckets
# Executes: aws s3 ls --profile iam-user
```

### Testing in Personal Account:
```powershell
python switch_mode.py root
python main.py
> create bucket test-bucket
# Executes: aws s3 mb s3://test-bucket --profile root-account
```

---

## ✅ What Changed from .env Method?

| Before (.env) | Now (AWS Profiles) |
|---------------|-------------------|
| `.env` file with all credentials | `~/.aws/credentials` (AWS standard) |
| `AWS_AUTH_METHOD=iam` | `mode = iam` in `config.ini` |
| `AWS_ACCESS_KEY_ID=...` | Managed by `aws configure` |
| Risk of committing secrets | Credentials outside project |
| Manual encryption needed | AWS CLI handles security |

---

## 🔐 Security Benefits

✅ **AWS credentials never in project folder**
✅ **Standard AWS CLI practice**
✅ **Easy to use multiple AWS accounts**
✅ **Works with all AWS tools**
✅ **Less risk of accidental commits**
✅ **`config.ini` only has mode + Gemini key**

---

## 🐛 Troubleshooting

### "Profile not found":
```powershell
aws configure list-profiles
aws configure --profile iam-user
```

### "Invalid Gemini API key":
Edit `config.ini` and add your actual key.

### "Permission denied":
Your IAM user doesn't have required permissions. Check IAM policies.

### Check credentials:
```powershell
python credential_manager.py
```

---

## 📚 Full Documentation

- **Complete Setup:** See `SETUP_AWS_PROFILES.md`
- **Project Guide:** See `Documentation/PROJECT_GUIDE.md`
- **AWS Integration:** See `Documentation/AWS_INTEGRATION.md`

---

**Ready to start? Run:** `python switch_mode.py status` **then** `python main.py` 🚀
