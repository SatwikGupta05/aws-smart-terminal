# 🎯 Quick Reference: Dual Authentication

## 📋 Copy-Paste Templates

### Template 1: IAM User Only (Recommended) ✅
```env
# Authentication method
AWS_AUTH_METHOD=iam

# IAM User Credentials
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_DEFAULT_REGION=us-east-1

# Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Terminal Settings
HISTORY_FILE=.terminal_history
MAX_HISTORY_ENTRIES=1000
```

---

### Template 2: Root Account Only (Not Recommended) ⚠️
```env
# Authentication method - ROOT ACCOUNT (NOT RECOMMENDED!)
AWS_AUTH_METHOD=root

# Root Account Credentials (FULL ACCESS TO EVERYTHING!)
AWS_ROOT_ACCESS_KEY_ID=AKIAI44QH8DHBEXAMPLE
AWS_ROOT_SECRET_ACCESS_KEY=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
AWS_DEFAULT_REGION=us-east-1

# Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Terminal Settings
HISTORY_FILE=.terminal_history
MAX_HISTORY_ENTRIES=1000
```

---

### Template 3: Both IAM and Root (Flexible) 🔄
```env
# Authentication method - Change this line to switch!
AWS_AUTH_METHOD=iam

# IAM User Credentials (Use for daily operations)
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_DEFAULT_REGION=us-east-1

# Root Account Credentials (Use only when absolutely necessary)
AWS_ROOT_ACCESS_KEY_ID=AKIAI44QH8DHBEXAMPLE
AWS_ROOT_SECRET_ACCESS_KEY=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY

# Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Terminal Settings
HISTORY_FILE=.terminal_history
MAX_HISTORY_ENTRIES=1000
```

---

## 🔄 How to Switch (Template 3)

**Currently using IAM, want to switch to Root:**
```env
# Just change this line from:
AWS_AUTH_METHOD=iam

# To this:
AWS_AUTH_METHOD=root
```

**Currently using Root, want to switch back to IAM:**
```env
# Just change this line from:
AWS_AUTH_METHOD=root

# Back to this:
AWS_AUTH_METHOD=iam
```

Then restart terminal: `python main.py`

---

## 🎨 Visual Guide

### What You See When Using IAM ✅
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  🚀 AI-Powered AWS Smart Terminal                  │
│                                                     │
│  Type commands in natural language, use ! for      │
│  shell, ? for help                                 │
│                                                     │
│  🔐 Authenticated as: IAM User  ← GREEN, SAFE      │
│                                                     │
│  Commands: home | history | clear | exit           │
│                                                     │
└─────────────────────────────────────────────────────┘

⚡ AWS ➜ 
```

### What You See When Using Root ⚠️
```
⚠️  WARNING: Using AWS ROOT account credentials!
⚠️  Root account has FULL access to ALL AWS resources.
⚠️  This is NOT recommended for security reasons.
⚠️  Consider using IAM user with limited permissions instead.

┌─────────────────────────────────────────────────────┐
│                                                     │
│  🚀 AI-Powered AWS Smart Terminal                  │
│                                                     │
│  Type commands in natural language, use ! for      │
│  shell, ? for help                                 │
│                                                     │
│  🔐 Authenticated as: ROOT ACCOUNT ⚠️              │
│                         (Not Recommended) ← RED     │
│                                                     │
│  Commands: home | history | clear | exit           │
│                                                     │
└─────────────────────────────────────────────────────┘

⚡ AWS ➜ 
```

---

## 🎯 Decision Flowchart

```
Do you have an IAM user?
        │
        ├─ YES ──────────────────────────────────┐
        │                                        │
        │                                        ▼
        │                              Use IAM (Recommended) ✅
        │                              AWS_AUTH_METHOD=iam
        │
        └─ NO ────┐
                  │
                  ▼
          Do you need to create IAM user?
                  │
                  ├─ YES ──────────────────┐
                  │                        │
                  │                        ▼
                  │               1. Start with Root ⚠️
                  │                  AWS_AUTH_METHOD=root
                  │               
                  │               2. Create IAM user
                  │                  (use terminal help)
                  │               
                  │               3. Switch to IAM ✅
                  │                  AWS_AUTH_METHOD=iam
                  │               
                  │               4. Delete root keys
                  │
                  └─ NO ───────────────────┐
                                          │
                                          ▼
                          Use Root (Not ideal) ⚠️
                          AWS_AUTH_METHOD=root
```

---

## 📝 Step-by-Step: First Time Setup

### If You Have IAM User:
```powershell
# 1. Copy template
copy .env.example .env

# 2. Edit .env
notepad .env

# 3. Set these values:
AWS_AUTH_METHOD=iam
AWS_ACCESS_KEY_ID=your_iam_key
AWS_SECRET_ACCESS_KEY=your_iam_secret

# 4. Run terminal
python main.py

# 5. Test
> list all S3 buckets
```

### If You Only Have Root:
```powershell
# 1. Copy template
copy .env.example .env

# 2. Edit .env
notepad .env

# 3. Set these values:
AWS_AUTH_METHOD=root
AWS_ROOT_ACCESS_KEY_ID=your_root_key
AWS_ROOT_SECRET_ACCESS_KEY=your_root_secret

# 4. Run terminal
python main.py

# 5. Create IAM user (recommended!)
> ?how do I create an IAM user

# 6. Once IAM user created, add to .env:
AWS_ACCESS_KEY_ID=new_iam_key
AWS_SECRET_ACCESS_KEY=new_iam_secret

# 7. Switch to IAM:
AWS_AUTH_METHOD=iam

# 8. Restart and test
python main.py
> list all S3 buckets

# 9. Delete root access keys from AWS Console
```

---

## ⚡ Quick Commands Reference

### Check Current Auth Method:
Terminal shows on welcome screen:
```
🔐 Authenticated as: IAM User
```
or
```
🔐 Authenticated as: ROOT ACCOUNT ⚠️  (Not Recommended)
```

### Ask Terminal About Auth:
```
> ?what authentication method am I using
> ?should I use IAM or root account
> ?how do I create an IAM user
> ?how do I switch from root to IAM
```

---

## 🔐 Security Checklist

### Using IAM (Recommended):
- [x] `AWS_AUTH_METHOD=iam` in .env
- [x] IAM user has minimum required permissions
- [x] MFA enabled on IAM user (in AWS Console)
- [x] Access keys rotated every 90 days
- [x] No root access keys stored

### Using Root (If You Must):
- [x] `AWS_AUTH_METHOD=root` in .env
- [x] MFA enabled on root account
- [x] Only use for tasks that require root
- [x] Plan to switch to IAM ASAP
- [x] Delete root keys after creating IAM user

---

## 🆘 Troubleshooting

### Error: "AWS credentials not found"
```
Problem: Missing credentials for selected auth method

If using IAM (AWS_AUTH_METHOD=iam):
✓ Check AWS_ACCESS_KEY_ID is set
✓ Check AWS_SECRET_ACCESS_KEY is set

If using Root (AWS_AUTH_METHOD=root):
✓ Check AWS_ROOT_ACCESS_KEY_ID is set
✓ Check AWS_ROOT_SECRET_ACCESS_KEY is set
```

### Error: "Access Denied"
```
Problem: IAM user lacks permissions

Solution 1: Add permissions to IAM user in AWS Console
Solution 2: Temporarily switch to root
            AWS_AUTH_METHOD=root
            (then fix IAM permissions and switch back)
```

### Warning Messages Won't Go Away
```
Problem: Using root account

Solution: These warnings are intentional!
          Switch to IAM to remove warnings:
          AWS_AUTH_METHOD=iam
```

---

## 📊 Comparison at a Glance

| What | IAM User | Root Account |
|------|----------|--------------|
| `.env` variable | `AWS_AUTH_METHOD=iam` | `AWS_AUTH_METHOD=root` |
| Credentials | `AWS_ACCESS_KEY_ID`<br>`AWS_SECRET_ACCESS_KEY` | `AWS_ROOT_ACCESS_KEY_ID`<br>`AWS_ROOT_SECRET_ACCESS_KEY` |
| Access Level | Limited (configurable) | Full (everything) |
| Security | ✅ High | ⚠️ Low |
| Recommended | ✅ YES | ❌ NO |
| Display Color | 🟢 Green | 🔴 Red |
| Warnings | None | Multiple |
| Best For | Daily use | Initial setup only |

---

## 💡 Pro Tips

1. **Keep Both**: Store both IAM and root credentials in .env for easy switching
2. **Default to IAM**: Set `AWS_AUTH_METHOD=iam` as default
3. **Root for Setup**: Use root only to create IAM user, then switch
4. **Delete Root Keys**: After creating IAM, delete root access keys from AWS
5. **Color Coding**: Green = safe (IAM), Red = danger (Root)
6. **Ask AI**: Terminal can help you create IAM users and set permissions

---

## 📖 More Information

- **Complete Guide**: [AUTH_GUIDE.md](AUTH_GUIDE.md)
- **Setup Guide**: [QUICKSTART.md](QUICKSTART.md)
- **What Changed**: [UPDATE_AUTH.md](UPDATE_AUTH.md)

---

**Remember:** IAM = Safe ✅ | Root = Risky ⚠️

Choose wisely! 🛡️
