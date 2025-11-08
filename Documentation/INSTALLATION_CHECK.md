# AI-Powered AWS Smart Terminal - Installation Verification

## ✅ Verify Your Installation

Run this checklist before using the terminal:

### 1. Python Version
```powershell
python --version
```
**Expected**: Python 3.8 or higher

### 2. Dependencies Installed
```powershell
pip list | Select-String "prompt-toolkit|rich|boto3|google-generativeai|python-dotenv"
```
**Expected**: All packages shown with version numbers

### 3. Environment File Exists
```powershell
Test-Path .env
```
**Expected**: True

### 4. Environment Variables Set
```powershell
Get-Content .env
```
**Expected**: Should see AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, GEMINI_API_KEY with actual values (not placeholders)

### 5. AWS Credentials Valid (Optional Test)
```powershell
# If you have AWS CLI installed
aws sts get-caller-identity
```
**Expected**: Your AWS account information

### 6. Test Run Examples
```powershell
python examples.py
```
**Expected**: List of example commands

### 7. Launch Terminal
```powershell
python main.py
```
**Expected**: ASCII art homepage and prompt

---

## 🔍 Troubleshooting

### Issue: Python not found
```powershell
# Install Python from python.org
# Or use Windows Store
winget install Python.Python.3.11
```

### Issue: Dependencies not installing
```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Try installing again
pip install -r requirements.txt
```

### Issue: Module import errors
```powershell
# Check which Python pip is using
pip --version

# Ensure it matches your python
python -c "import sys; print(sys.executable)"

# If different, use:
python -m pip install -r requirements.txt
```

### Issue: .env file not found
```powershell
# Copy the example
Copy-Item .env.example .env

# Edit with notepad
notepad .env
```

### Issue: AWS credentials error
```powershell
# Verify your credentials format in .env:
# AWS_ACCESS_KEY_ID=AKIA... (20 chars)
# AWS_SECRET_ACCESS_KEY=... (40 chars)
# No quotes, no spaces around =
```

### Issue: Gemini API error
```powershell
# Get a new API key from:
# https://makersuite.google.com/app/apikey
# 
# Add to .env as:
# GEMINI_API_KEY=your_key_here
```

---

## 🧪 Quick Functional Test

Once the terminal is running, try these commands in order:

### Test 1: Help System
```
> ?what is S3
```
**Expected**: AI response explaining S3

### Test 2: Shell Command
```
> !echo Hello from AWS Terminal
```
**Expected**: "Hello from AWS Terminal" printed

### Test 3: AWS List Operation (safest test)
```
> list all S3 buckets
```
**Expected**: Your S3 buckets listed (or empty list if none)

### Test 4: Command History
```
Press ↑ arrow key
```
**Expected**: Previous commands appear

### Test 5: Homepage
```
> home
```
**Expected**: ASCII art homepage redisplayed

### Test 6: Clear Screen
```
> clear
```
**Expected**: Screen cleared

### Test 7: Exit
```
> exit
```
**Expected**: Terminal exits gracefully

---

## 📊 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8 | 3.11+ |
| RAM | 512 MB | 2 GB |
| Storage | 100 MB | 500 MB |
| Internet | Required | High-speed |
| OS | Windows 10+ | Windows 11 |

---

## ✅ Pre-Launch Checklist

- [ ] Python 3.8+ installed
- [ ] All dependencies installed (`requirements.txt`)
- [ ] `.env` file created
- [ ] AWS credentials added to `.env`
- [ ] Gemini API key added to `.env`
- [ ] AWS credentials tested (optional)
- [ ] Example commands reviewed
- [ ] Documentation read (`README.md`, `QUICKSTART.md`)

---

## 🎉 Ready to Launch!

If all checks pass, you're ready to go! Run:

```powershell
python main.py
```

Enjoy your AI-Powered AWS Smart Terminal! 🚀☁️

---

## 📞 Need Help?

1. **Setup Issues**: See `QUICKSTART.md`
2. **Command Help**: See `COMMANDS.md`
3. **Technical Details**: See `DEV_NOTES.md`
4. **Full Overview**: See `PROJECT_SUMMARY.md`
5. **In-Terminal Help**: Type `?` followed by your question

---

**Note**: The import errors you see in VS Code are normal before installing dependencies. They will disappear after running `pip install -r requirements.txt`.
