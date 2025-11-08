# 🔐 AWS Authentication Options

## Overview

This terminal supports **two authentication methods**:
1. **IAM User** (Recommended) ✅
2. **Root Account** (Not Recommended) ⚠️

---

## Method 1: IAM User (RECOMMENDED) ✅

### Why Use IAM?
- ✅ **Better Security**: Limited permissions (principle of least privilege)
- ✅ **Auditable**: Track who does what
- ✅ **Revocable**: Can disable without affecting other users
- ✅ **Best Practice**: AWS recommends this approach
- ✅ **MFA Support**: Can enable multi-factor authentication

### Setup IAM Authentication

**1. Edit your `.env` file:**
```env
# Set authentication method to IAM
AWS_AUTH_METHOD=iam

# Your IAM user credentials
AWS_ACCESS_KEY_ID=AKIA...your_iam_key_here
AWS_SECRET_ACCESS_KEY=your_iam_secret_here
AWS_DEFAULT_REGION=us-east-1
```

**2. Create IAM User (if you don't have one):**
```
1. Go to AWS Console → IAM → Users
2. Click "Add users"
3. Enter username (e.g., "terminal-user")
4. Select "Programmatic access"
5. Attach policies based on what you need:
   - PowerUserAccess (recommended for development)
   - Or specific service permissions
6. Save the Access Key ID and Secret Access Key
7. Add them to your .env file
```

**3. Required IAM Permissions:**

For full terminal functionality, your IAM user needs:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "ec2:Describe*",
        "ec2:RunInstances",
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:TerminateInstances",
        "lambda:List*",
        "lambda:Invoke*",
        "rds:Describe*",
        "iam:List*",
        "cloudwatch:List*",
        "dynamodb:List*",
        "sns:List*",
        "sqs:List*"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## Method 2: Root Account (NOT RECOMMENDED) ⚠️

### ⚠️ WARNING: Security Risks
- ❌ **Full Access**: Unrestricted access to ALL AWS resources
- ❌ **Cannot Limit**: No way to restrict permissions
- ❌ **High Risk**: If compromised, entire AWS account is at risk
- ❌ **Against Best Practices**: AWS strongly discourages this
- ❌ **Compliance Issues**: May violate security policies

### When You Might Need Root
- Creating IAM users (initial setup only)
- Changing account settings
- Closing AWS account
- Certain billing operations

### Setup Root Authentication

**⚠️ Only use this if absolutely necessary!**

**1. Edit your `.env` file:**
```env
# Set authentication method to root (NOT RECOMMENDED!)
AWS_AUTH_METHOD=root

# Your AWS root account credentials
AWS_ROOT_ACCESS_KEY_ID=your_root_access_key_here
AWS_ROOT_SECRET_ACCESS_KEY=your_root_secret_key_here
AWS_DEFAULT_REGION=us-east-1

# Keep IAM credentials here for switching back
AWS_ACCESS_KEY_ID=your_iam_key_here
AWS_SECRET_ACCESS_KEY=your_iam_secret_here
```

**2. Get Root Credentials:**
```
1. Go to AWS Console
2. Sign in as root user (your account email)
3. Click account name (top right) → Security Credentials
4. Under "Access Keys", create new access key
5. ⚠️ STORE SECURELY - these are root credentials!
6. Add to .env file
```

**3. Terminal Will Show Warning:**
```
⚠️  WARNING: Using AWS ROOT account credentials!
⚠️  Root account has FULL access to ALL AWS resources.
⚠️  This is NOT recommended for security reasons.
⚠️  Consider using IAM user with limited permissions instead.

🔐 Authenticated as: ROOT ACCOUNT ⚠️  (Not Recommended)
```

---

## Switching Between Methods

### Switch to IAM (Recommended):
```env
AWS_AUTH_METHOD=iam
```

### Switch to Root (Not Recommended):
```env
AWS_AUTH_METHOD=root
```

Just change the `AWS_AUTH_METHOD` variable and restart the terminal!

---

## Security Best Practices

### For IAM Users (Do This) ✅
```
✅ Use IAM users instead of root
✅ Enable MFA (Multi-Factor Authentication)
✅ Grant minimum required permissions
✅ Rotate access keys regularly (every 90 days)
✅ Use different IAM users for different purposes
✅ Monitor access with CloudTrail
✅ Never share credentials
✅ Store credentials securely (.env file, not in code)
```

### For Root Account (If You Must Use It) ⚠️
```
⚠️ Use ONLY when absolutely necessary
⚠️ Enable MFA immediately
⚠️ Use a strong, unique password
⚠️ Don't use for daily operations
⚠️ Delete root access keys after use
⚠️ Log out after completing root tasks
⚠️ Switch back to IAM user ASAP
```

---

## Comparison Table

| Feature | IAM User ✅ | Root Account ⚠️ |
|---------|------------|------------------|
| **Security** | Limited permissions | Full access |
| **Best Practice** | ✅ Recommended | ❌ Not recommended |
| **Revocable** | ✅ Yes | ❌ Cannot revoke root |
| **Auditable** | ✅ Yes | ⚠️ Harder to audit |
| **MFA** | ✅ Supported | ✅ Supported |
| **Permission Control** | ✅ Granular | ❌ All or nothing |
| **Multiple Users** | ✅ Create many | ❌ Only one root |
| **Compliance** | ✅ Meets standards | ❌ May violate policies |

---

## Example .env Configurations

### Configuration 1: IAM Only (Recommended)
```env
AWS_AUTH_METHOD=iam
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_DEFAULT_REGION=us-east-1

GEMINI_API_KEY=your_gemini_key_here
```

### Configuration 2: Both IAM and Root (Switching)
```env
# Current method (change this line to switch)
AWS_AUTH_METHOD=iam

# IAM User Credentials (Recommended for daily use)
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_DEFAULT_REGION=us-east-1

# Root Account Credentials (Use only when necessary)
AWS_ROOT_ACCESS_KEY_ID=AKIAI44QH8DHBEXAMPLE
AWS_ROOT_SECRET_ACCESS_KEY=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY

GEMINI_API_KEY=your_gemini_key_here
```

---

## Terminal Commands to Check Auth

### View Current Authentication:
The terminal displays your auth method on the welcome screen:
```
🔐 Authenticated as: IAM User
```
or
```
🔐 Authenticated as: ROOT ACCOUNT ⚠️  (Not Recommended)
```

### Ask Terminal About Your Auth:
```
> ?what AWS account am I using
```

The AI will explain your current authentication method.

---

## Troubleshooting

### Error: "AWS credentials not found"
**If using IAM:**
- Check `AWS_AUTH_METHOD=iam` in .env
- Verify `AWS_ACCESS_KEY_ID` is set
- Verify `AWS_SECRET_ACCESS_KEY` is set

**If using Root:**
- Check `AWS_AUTH_METHOD=root` in .env
- Verify `AWS_ROOT_ACCESS_KEY_ID` is set
- Verify `AWS_ROOT_SECRET_ACCESS_KEY` is set

### Error: "Access Denied"
**If using IAM:**
- Your IAM user lacks required permissions
- Add necessary policies in AWS Console
- Or temporarily switch to root (not recommended)

**If using Root:**
- Verify credentials are correct
- Check if root access keys are active

### How to Test Credentials:
```powershell
# Test IAM credentials
$env:AWS_ACCESS_KEY_ID="your_iam_key"
$env:AWS_SECRET_ACCESS_KEY="your_iam_secret"
aws sts get-caller-identity

# Test Root credentials
$env:AWS_ACCESS_KEY_ID="your_root_key"
$env:AWS_SECRET_ACCESS_KEY="your_root_secret"
aws sts get-caller-identity
```

---

## Migration Path: Root → IAM

### Step-by-Step Migration:

**1. While Using Root, Create IAM User:**
```
> ?how do I create an IAM user
```
Follow AI instructions

**2. Save IAM Credentials:**
Add to .env file under `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

**3. Test IAM User:**
Switch to IAM mode and test:
```env
AWS_AUTH_METHOD=iam
```

**4. Delete Root Access Keys:**
Once IAM works, delete root access keys from AWS Console

**5. Update .env:**
Remove or comment out root credentials:
```env
AWS_AUTH_METHOD=iam

AWS_ACCESS_KEY_ID=your_iam_key
AWS_SECRET_ACCESS_KEY=your_iam_secret

# Root credentials removed for security
# AWS_ROOT_ACCESS_KEY_ID=
# AWS_ROOT_SECRET_ACCESS_KEY=
```

---

## Quick Reference

### To Use IAM (Recommended):
```env
AWS_AUTH_METHOD=iam
AWS_ACCESS_KEY_ID=your_iam_key
AWS_SECRET_ACCESS_KEY=your_iam_secret
```

### To Use Root (Not Recommended):
```env
AWS_AUTH_METHOD=root
AWS_ROOT_ACCESS_KEY_ID=your_root_key
AWS_ROOT_SECRET_ACCESS_KEY=your_root_secret
```

### To Switch:
Just change `AWS_AUTH_METHOD` and restart terminal!

---

## Summary

✅ **Use IAM** for daily operations  
⚠️ **Use Root** only when absolutely necessary  
🔄 **Easy switching** between both methods  
🔐 **Terminal shows** which method you're using  
📝 **Keep both** credentials in .env for flexibility  

**Remember:** Root account = **full power** = **high risk** ⚠️

Stay safe! Use IAM whenever possible! 🛡️
