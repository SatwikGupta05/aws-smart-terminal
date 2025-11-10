# 🔐 AWS Authentication Guide# 🔐 AWS Authentication Options



## Overview> **⚠️ DEPRECATION NOTICE**: This document describes the old `.env` file authentication method.  

> **🆕 NEW METHOD**: We now use AWS CLI Profiles (standard method).  

This terminal uses **AWS CLI Profiles** (AWS standard method) for authentication. You can configure multiple profiles for different access levels:> **📖 See**: [SETUP_AWS_PROFILES.md](../SETUP_AWS_PROFILES.md) for current setup instructions.



1. **IAM User** (Recommended) ✅## Overview

2. **Root Account** (Not Recommended) ⚠️

3. **Demo Mode** (No AWS credentials needed) 🎮This terminal supports **two authentication methods**:

1. **IAM User** (Recommended) ✅

---2. **Root Account** (Not Recommended) ⚠️



## Method 1: IAM User (RECOMMENDED) ✅---



### Why Use IAM?## Method 1: IAM User (RECOMMENDED) ✅

- ✅ **Better Security**: Limited permissions (principle of least privilege)

- ✅ **Auditable**: Track who does what### Why Use IAM?

- ✅ **Revocable**: Can disable without affecting other users- ✅ **Better Security**: Limited permissions (principle of least privilege)

- ✅ **Best Practice**: AWS recommends this approach- ✅ **Auditable**: Track who does what

- ✅ **MFA Support**: Can enable multi-factor authentication- ✅ **Revocable**: Can disable without affecting other users

- ✅ **Best Practice**: AWS recommends this approach

### Setup IAM Authentication- ✅ **MFA Support**: Can enable multi-factor authentication



**1. Create IAM User (if you don't have one):**### Setup IAM Authentication

```

1. Go to AWS Console → IAM → Users**1. Edit your `.env` file:**

2. Click "Add users"```env

3. Enter username (e.g., "terminal-user")# Set authentication method to IAM

4. Select "Programmatic access"AWS_AUTH_METHOD=iam

5. Attach policies based on what you need:

   - PowerUserAccess (recommended for development)# Your IAM user credentials

   - Or specific service permissionsAWS_ACCESS_KEY_ID=AKIA...your_iam_key_here

6. Save the Access Key ID and Secret Access KeyAWS_SECRET_ACCESS_KEY=your_iam_secret_here

```AWS_DEFAULT_REGION=us-east-1

```

**2. Configure AWS CLI Profile:**

```bash**2. Create IAM User (if you don't have one):**

aws configure --profile iam-user```

# Enter your AWS Access Key ID1. Go to AWS Console → IAM → Users

# Enter your AWS Secret Access Key2. Click "Add users"

# Enter default region (e.g., us-east-1)3. Enter username (e.g., "terminal-user")

# Enter output format (json recommended)4. Select "Programmatic access"

```5. Attach policies based on what you need:

   - PowerUserAccess (recommended for development)

**3. Update config.ini:**   - Or specific service permissions

```ini6. Save the Access Key ID and Secret Access Key

[AUTH]7. Add them to your .env file

mode = iam```



[AWS]**3. Required IAM Permissions:**

iam_profile = iam-user

```For full terminal functionality, your IAM user needs:

```json

**4. Verify setup:**{

```bash  "Version": "2012-10-17",

python main.py  "Statement": [

# Should connect using your IAM user credentials    {

```      "Effect": "Allow",

      "Action": [

**Required IAM Permissions:**        "s3:*",

        "ec2:Describe*",

For full terminal functionality, your IAM user needs:        "ec2:RunInstances",

```json        "ec2:StartInstances",

{        "ec2:StopInstances",

  "Version": "2012-10-17",        "ec2:TerminateInstances",

  "Statement": [        "lambda:List*",

    {        "lambda:Invoke*",

      "Effect": "Allow",        "rds:Describe*",

      "Action": [        "iam:List*",

        "s3:*",        "cloudwatch:List*",

        "ec2:Describe*",        "dynamodb:List*",

        "ec2:RunInstances",        "sns:List*",

        "ec2:StartInstances",        "sqs:List*"

        "ec2:StopInstances",      ],

        "ec2:TerminateInstances",      "Resource": "*"

        "lambda:List*",    }

        "lambda:Invoke*",  ]

        "rds:Describe*",}

        "iam:List*",```

        "cloudwatch:List*",

        "dynamodb:List*",---

        "sns:List*",

        "sqs:List*"## Method 2: Root Account (NOT RECOMMENDED) ⚠️

      ],

      "Resource": "*"### ⚠️ WARNING: Security Risks

    }- ❌ **Full Access**: Unrestricted access to ALL AWS resources

  ]- ❌ **Cannot Limit**: No way to restrict permissions

}- ❌ **High Risk**: If compromised, entire AWS account is at risk

```- ❌ **Against Best Practices**: AWS strongly discourages this

- ❌ **Compliance Issues**: May violate security policies

---

### When You Might Need Root

## Method 2: Root Account (NOT RECOMMENDED) ⚠️- Creating IAM users (initial setup only)

- Changing account settings

### ⚠️ WARNING: Security Risks- Closing AWS account

- ❌ **Full Access**: Unrestricted access to ALL AWS resources- Certain billing operations

- ❌ **Cannot Limit**: No way to restrict permissions

- ❌ **High Risk**: If compromised, entire AWS account is at risk### Setup Root Authentication

- ❌ **Against Best Practices**: AWS strongly discourages this

- ❌ **Compliance Issues**: May violate security policies**⚠️ Only use this if absolutely necessary!**



### When You Might Need Root**1. Edit your `.env` file:**

- Creating IAM users (initial setup only)```env

- Changing account settings# Set authentication method to root (NOT RECOMMENDED!)

- Closing AWS accountAWS_AUTH_METHOD=root

- Certain billing operations

# Your AWS root account credentials

### Setup Root AuthenticationAWS_ROOT_ACCESS_KEY_ID=your_root_access_key_here

AWS_ROOT_SECRET_ACCESS_KEY=your_root_secret_key_here

**⚠️ Only use this if absolutely necessary!**AWS_DEFAULT_REGION=us-east-1



**1. Configure AWS CLI Profile:**# Keep IAM credentials here for switching back

```bashAWS_ACCESS_KEY_ID=your_iam_key_here

aws configure --profile root-accountAWS_SECRET_ACCESS_KEY=your_iam_secret_here

# Enter your root AWS Access Key ID```

# Enter your root AWS Secret Access Key

# Enter default region (e.g., us-east-1)**2. Get Root Credentials:**

# Enter output format (json recommended)```

```1. Go to AWS Console

2. Sign in as root user (your account email)

**2. Update config.ini:**3. Click account name (top right) → Security Credentials

```ini4. Under "Access Keys", create new access key

[AUTH]5. ⚠️ STORE SECURELY - these are root credentials!

mode = root6. Add to .env file

```

[AWS]

root_profile = root-account**3. Terminal Will Show Warning:**

``````

⚠️  WARNING: Using AWS ROOT account credentials!

**3. Verify setup:**⚠️  Root account has FULL access to ALL AWS resources.

```bash⚠️  This is NOT recommended for security reasons.

python main.py⚠️  Consider using IAM user with limited permissions instead.

# Should connect using root account credentials

```🔐 Authenticated as: ROOT ACCOUNT ⚠️  (Not Recommended)

```

---

---

## Method 3: Demo Mode (NO AWS CREDENTIALS) 🎮

## Switching Between Methods

### What is Demo Mode?

- ✅ **No AWS Account Needed**: Test the terminal without real credentials### Switch to IAM (Recommended):

- ✅ **Safe Testing**: Commands are simulated, nothing actually executes```env

- ✅ **Learning Tool**: Perfect for learning AWS commandsAWS_AUTH_METHOD=iam

- ✅ **No Costs**: Zero AWS charges```



### Setup Demo Mode### Switch to Root (Not Recommended):

```env

**1. Update config.ini:**AWS_AUTH_METHOD=root

```ini```

[AUTH]

mode = demoJust change the `AWS_AUTH_METHOD` variable and restart the terminal!



[GEMINI]---

api_key = your_gemini_api_key_here

```## Security Best Practices



**2. Run terminal:**### For IAM Users (Do This) ✅

```bash```

python main.py✅ Use IAM users instead of root

# Will run in demo mode - no AWS operations executed✅ Enable MFA (Multi-Factor Authentication)

```✅ Grant minimum required permissions

✅ Rotate access keys regularly (every 90 days)

---✅ Use different IAM users for different purposes

✅ Monitor access with CloudTrail

## Switching Between Modes✅ Never share credentials

✅ Store credentials securely (.env file, not in code)

Use the `switch_mode.py` utility to easily switch authentication modes:```



```bash### For Root Account (If You Must Use It) ⚠️

# Switch to Demo Mode```

python switch_mode.py demo⚠️ Use ONLY when absolutely necessary

⚠️ Enable MFA immediately

# Switch to IAM Mode⚠️ Use a strong, unique password

python switch_mode.py iam⚠️ Don't use for daily operations

⚠️ Delete root access keys after use

# Switch to Root Mode⚠️ Log out after completing root tasks

python switch_mode.py root⚠️ Switch back to IAM user ASAP

```

# Check current mode

python switch_mode.py---

```

## Comparison Table

---

| Feature | IAM User ✅ | Root Account ⚠️ |

## AWS CLI Profiles Location|---------|------------|------------------|

| **Security** | Limited permissions | Full access |

Your AWS credentials are stored in:| **Best Practice** | ✅ Recommended | ❌ Not recommended |

| **Revocable** | ✅ Yes | ❌ Cannot revoke root |

**Windows:**| **Auditable** | ✅ Yes | ⚠️ Harder to audit |

```| **MFA** | ✅ Supported | ✅ Supported |

C:\Users\YourUsername\.aws\credentials| **Permission Control** | ✅ Granular | ❌ All or nothing |

C:\Users\YourUsername\.aws\config| **Multiple Users** | ✅ Create many | ❌ Only one root |

```| **Compliance** | ✅ Meets standards | ❌ May violate policies |



**Mac/Linux:**---

```

~/.aws/credentials## Example .env Configurations

~/.aws/config

```### Configuration 1: IAM Only (Recommended)

```env

### Example credentials file:AWS_AUTH_METHOD=iam

```iniAWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE

[iam-user]AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

aws_access_key_id = AKIA...AWS_DEFAULT_REGION=us-east-1

aws_secret_access_key = ...

GEMINI_API_KEY=your_gemini_key_here

[root-account]```

aws_access_key_id = AKIA...

aws_secret_access_key = ...### Configuration 2: Both IAM and Root (Switching)

``````env

# Current method (change this line to switch)

---AWS_AUTH_METHOD=iam



## Security Best Practices# IAM User Credentials (Recommended for daily use)

AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE

### ✅ DO:AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

- Use IAM users with minimal required permissionsAWS_DEFAULT_REGION=us-east-1

- Enable MFA on your AWS account

- Rotate access keys regularly (every 90 days)# Root Account Credentials (Use only when necessary)

- Use different profiles for different projectsAWS_ROOT_ACCESS_KEY_ID=AKIAI44QH8DHBEXAMPLE

- Keep `config.ini` out of version control (it's gitignored)AWS_ROOT_SECRET_ACCESS_KEY=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY



### ❌ DON'T:GEMINI_API_KEY=your_gemini_key_here

- Use root account for day-to-day operations```

- Share AWS credentials

- Commit credentials to Git---

- Use overly permissive IAM policies

- Leave unused access keys active## Terminal Commands to Check Auth



---### View Current Authentication:

The terminal displays your auth method on the welcome screen:

## Troubleshooting```

🔐 Authenticated as: IAM User

### Profile not found error```

**Error:** `AWS CLI not configured for profile: iam-user`or

```

**Solution:**🔐 Authenticated as: ROOT ACCOUNT ⚠️  (Not Recommended)

```bash```

# List configured profiles

aws configure list-profiles### Ask Terminal About Your Auth:

```

# Configure missing profile> ?what AWS account am I using

aws configure --profile iam-user```

```

The AI will explain your current authentication method.

### Invalid credentials

**Error:** `Invalid AWS credentials`---



**Solution:**## Troubleshooting

```bash

# Test credentials### Error: "AWS credentials not found"

aws sts get-caller-identity --profile iam-user**If using IAM:**

- Check `AWS_AUTH_METHOD=iam` in .env

# Reconfigure if needed- Verify `AWS_ACCESS_KEY_ID` is set

aws configure --profile iam-user- Verify `AWS_SECRET_ACCESS_KEY` is set

```

**If using Root:**

### Wrong region- Check `AWS_AUTH_METHOD=root` in .env

**Error:** `Service not available in region`- Verify `AWS_ROOT_ACCESS_KEY_ID` is set

- Verify `AWS_ROOT_SECRET_ACCESS_KEY` is set

**Solution:**

```bash### Error: "Access Denied"

# Update region**If using IAM:**

aws configure set region us-east-1 --profile iam-user- Your IAM user lacks required permissions

```- Add necessary policies in AWS Console

- Or temporarily switch to root (not recommended)

---

**If using Root:**

## Additional Resources- Verify credentials are correct

- Check if root access keys are active

- [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

- [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)### How to Test Credentials:

- [IAM Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)```powershell

# Test IAM credentials

---$env:AWS_ACCESS_KEY_ID="your_iam_key"

$env:AWS_SECRET_ACCESS_KEY="your_iam_secret"

For quick setup, see [QUICKSTART_AWS_PROFILES.md](../QUICKSTART_AWS_PROFILES.md)aws sts get-caller-identity

For detailed setup, see [SETUP_AWS_PROFILES.md](../SETUP_AWS_PROFILES.md)

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
