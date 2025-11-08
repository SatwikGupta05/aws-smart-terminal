# ✅ DUAL AUTHENTICATION UPDATE

## What's New?

Your AI-Powered AWS Smart Terminal now supports **BOTH** authentication methods:

1. ✅ **IAM User** (Recommended - secure, limited permissions)
2. ⚠️ **Root Account** (Available but not recommended - full access)

---

## Quick Setup Guide

### Step 1: Edit Your `.env` File

You have two options:

#### Option A: Use IAM User (Recommended) ✅
```env
AWS_AUTH_METHOD=iam
AWS_ACCESS_KEY_ID=your_iam_access_key_here
AWS_SECRET_ACCESS_KEY=your_iam_secret_key_here
AWS_DEFAULT_REGION=us-east-1
GEMINI_API_KEY=your_gemini_key_here
```

#### Option B: Use Root Account (Not Recommended) ⚠️
```env
AWS_AUTH_METHOD=root
AWS_ROOT_ACCESS_KEY_ID=your_root_access_key_here
AWS_ROOT_SECRET_ACCESS_KEY=your_root_secret_key_here
AWS_DEFAULT_REGION=us-east-1
GEMINI_API_KEY=your_gemini_key_here
```

#### Option C: Keep Both & Switch Easily 🔄
```env
# Change this line to switch between IAM and Root
AWS_AUTH_METHOD=iam

# IAM User Credentials (for daily use)
AWS_ACCESS_KEY_ID=your_iam_key
AWS_SECRET_ACCESS_KEY=your_iam_secret

# Root Account Credentials (for when needed)
AWS_ROOT_ACCESS_KEY_ID=your_root_key
AWS_ROOT_SECRET_ACCESS_KEY=your_root_secret

AWS_DEFAULT_REGION=us-east-1
GEMINI_API_KEY=your_gemini_key_here
```

---

## What You'll See

### When Using IAM (Recommended):
```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  🚀 AI-Powered AWS Smart Terminal                        ║
║  Type commands in natural language, use ! for shell,     ║
║  ? for help                                               ║
║  🔐 Authenticated as: IAM User                           ║
║  Commands: home | history | clear | exit                 ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

### When Using Root (Not Recommended):
```
⚠️  WARNING: Using AWS ROOT account credentials!
⚠️  Root account has FULL access to ALL AWS resources.
⚠️  This is NOT recommended for security reasons.
⚠️  Consider using IAM user with limited permissions instead.

╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  🚀 AI-Powered AWS Smart Terminal                        ║
║  Type commands in natural language, use ! for shell,     ║
║  ? for help                                               ║
║  🔐 Authenticated as: ROOT ACCOUNT ⚠️  (Not Recommended) ║
║  Commands: home | history | clear | exit                 ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Files Updated

### 1. `.env.example` - Configuration Template
- ✅ Added `AWS_AUTH_METHOD` option
- ✅ Added IAM credentials section
- ✅ Added Root credentials section
- ✅ Added warnings about root usage

### 2. `aws_handler.py` - AWS Client Handler
- ✅ Added auth method detection
- ✅ Added credential selection logic
- ✅ Added warning messages for root usage
- ✅ Tracks authentication type for display

### 3. `main.py` - Terminal Engine
- ✅ Displays current auth method on welcome screen
- ✅ Shows warning indicator for root account
- ✅ Color-coded auth status (green for IAM, red for root)

### 4. `AUTH_GUIDE.md` - NEW! Complete Authentication Guide
- ✅ Detailed explanation of both methods
- ✅ Security best practices
- ✅ Setup instructions for each method
- ✅ Comparison table
- ✅ Migration guide from root to IAM
- ✅ Troubleshooting section

### 5. `QUICKSTART.md` - Updated Setup Guide
- ✅ Added both authentication options
- ✅ References AUTH_GUIDE.md

### 6. `README.md` - Updated Main Docs
- ✅ Mentions dual authentication support
- ✅ Links to AUTH_GUIDE.md

---

## How to Switch Between IAM and Root

**It's super easy!** Just change one line in your `.env` file:

### Switch to IAM:
```env
AWS_AUTH_METHOD=iam
```
Then restart the terminal: `python main.py`

### Switch to Root:
```env
AWS_AUTH_METHOD=root
```
Then restart the terminal: `python main.py`

---

## Security Recommendations

### ✅ DO:
- Use IAM for daily operations
- Create IAM user with minimum required permissions
- Enable MFA on both IAM and root accounts
- Rotate credentials regularly
- Keep root credentials secure

### ⚠️ DON'T:
- Use root account for daily tasks
- Share root credentials
- Store root credentials in multiple places
- Leave root access keys active when not needed

---

## Example Workflow

### Scenario: You need root for initial setup, then switch to IAM

**1. Start with Root (if needed):**
```env
AWS_AUTH_METHOD=root
AWS_ROOT_ACCESS_KEY_ID=your_root_key
AWS_ROOT_SECRET_ACCESS_KEY=your_root_secret
```

**2. Use terminal to create IAM user:**
```
> ?how do I create an IAM user with PowerUser access
```
Follow the AI's instructions

**3. Add IAM credentials to .env:**
```env
AWS_ACCESS_KEY_ID=your_new_iam_key
AWS_SECRET_ACCESS_KEY=your_new_iam_secret
```

**4. Switch to IAM:**
```env
AWS_AUTH_METHOD=iam
```

**5. Test IAM access:**
```
python main.py
> list all S3 buckets
```

**6. Once confirmed, delete root access keys from AWS Console**

---

## Troubleshooting

### "AWS credentials not found"
- Check `AWS_AUTH_METHOD` matches your credential type
- For `iam`: ensure `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are set
- For `root`: ensure `AWS_ROOT_ACCESS_KEY_ID` and `AWS_ROOT_SECRET_ACCESS_KEY` are set

### "Access Denied" errors
- IAM user may lack required permissions
- Temporarily switch to root to fix permissions (not ideal, but works)
- Or use AWS Console to add policies to IAM user

### Warning messages about root
- These are intentional reminders
- They appear every time you use root account
- Switch to IAM to remove warnings

---

## Need More Help?

📖 **Read the Complete Guide:** [AUTH_GUIDE.md](AUTH_GUIDE.md)

This guide includes:
- Detailed security explanations
- Step-by-step IAM user creation
- Permission requirements
- Migration instructions
- Comparison tables
- Best practices

---

## Summary

✅ **You now have flexibility**: Use IAM (secure) or Root (when necessary)
✅ **Easy switching**: Just change `AWS_AUTH_METHOD` in .env
✅ **Clear warnings**: Terminal shows which method you're using
✅ **Full documentation**: AUTH_GUIDE.md has all the details
✅ **Best practices**: Encouraged to use IAM, warned about root

**Recommendation:** Start with root if you need to create IAM user, then switch to IAM for all regular operations.

---

🚀 **Your terminal is ready to use with either authentication method!**

Just update your `.env` file and run: `python main.py`
