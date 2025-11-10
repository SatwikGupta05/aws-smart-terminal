# AI-Powered AWS Smart Terminal - Installation Verification# AI-Powered AWS Smart Terminal - Installation Verification



## ✅ Verify Your Installation> **⚠️ NOTE**: This checklist references the old `.env` file method.  

> **🆕 CURRENT METHOD**: AWS CLI Profiles with `config.ini`. See [SETUP_AWS_PROFILES.md](../SETUP_AWS_PROFILES.md)

Run this checklist before using the terminal:

## ✅ Verify Your Installation (OLD METHOD - for reference)

### 1. Python Version

```powershellRun this checklist before using the terminal:

python --version

```### 1. Python Version

**Expected**: Python 3.8 or higher```powershell

python --version

### 2. Dependencies Installed```

```powershell**Expected**: Python 3.8 or higher

pip list | Select-String "prompt-toolkit|rich|boto3|google-generativeai"

```### 2. Dependencies Installed

**Expected**: All packages shown with version numbers```powershell

pip list | Select-String "prompt-toolkit|rich|boto3|google-generativeai|python-dotenv"

### 3. Configuration File Exists```

```powershell**Expected**: All packages shown with version numbers

Test-Path config.ini

```### 3. Environment File Exists

**Expected**: True```powershell

Test-Path .env

If False, create it:```

```powershell**Expected**: True

Copy-Item config.ini.example config.ini

# Then edit config.ini and add your Gemini API key### 4. Environment Variables Set

``````powershell

Get-Content .env

### 4. Configuration Valid```

```powershell**Expected**: Should see AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, GEMINI_API_KEY with actual values (not placeholders)

Get-Content config.ini

```### 5. AWS Credentials Valid (Optional Test)

**Expected**: Should see sections [AUTH], [GEMINI], [AWS] with appropriate values```powershell

# If you have AWS CLI installed

### 5. AWS CLI Installed (For IAM/Root Mode)aws sts get-caller-identity

```powershell```

aws --version**Expected**: Your AWS account information

```

**Expected**: AWS CLI version information### 6. Test Run Examples

```powershell

If not installed, download from: https://aws.amazon.com/cli/python examples.py

```

### 6. AWS Profile Configured (For IAM/Root Mode)**Expected**: List of example commands

```powershell

aws configure list-profiles### 7. Launch Terminal

``````powershell

**Expected**: Should see your configured profiles (e.g., iam-user, root-account)python main.py

```

If no profiles shown:**Expected**: ASCII art homepage and prompt

```powershell

aws configure --profile iam-user---

# Enter your AWS Access Key ID

# Enter your AWS Secret Access Key## 🔍 Troubleshooting

# Enter default region (e.g., us-east-1)

# Enter output format (json recommended)### Issue: Python not found

``````powershell

# Install Python from python.org

### 7. Test AWS Credentials (Optional)# Or use Windows Store

```powershellwinget install Python.Python.3.11

aws sts get-caller-identity --profile iam-user```

```

**Expected**: Your AWS account information (UserId, Account, Arn)### Issue: Dependencies not installing

```powershell

### 8. Test Run Examples# Upgrade pip first

```powershellpython -m pip install --upgrade pip

python examples.py

```# Try installing again

**Expected**: List of example commandspip install -r requirements.txt

```

### 9. Launch Terminal

```powershell### Issue: Module import errors

python main.py```powershell

```# Check which Python pip is using

**Expected**: ASCII art homepage and prompt showing your authentication modepip --version



---# Ensure it matches your python

python -c "import sys; print(sys.executable)"

## 🔧 Troubleshooting

# If different, use:

### Issue: Python not foundpython -m pip install -r requirements.txt

**Solution**: ```

```powershell

# Install Python from python.org### Issue: .env file not found

# Or use Windows Store```powershell

# Then restart terminal# Copy the example

```Copy-Item .env.example .env



### Issue: Dependencies missing# Edit with notepad

**Solution**:notepad .env

```powershell```

pip install -r requirements.txt

```### Issue: AWS credentials error

```powershell

### Issue: config.ini not found# Verify your credentials format in .env:

**Solution**:# AWS_ACCESS_KEY_ID=AKIA... (20 chars)

```powershell# AWS_SECRET_ACCESS_KEY=... (40 chars)

Copy-Item config.ini.example config.ini# No quotes, no spaces around =

notepad config.ini```

# Add your Gemini API key

```### Issue: Gemini API error

```powershell

### Issue: AWS CLI not found# Get a new API key from:

**Solution**:# https://makersuite.google.com/app/apikey

- Download and install from https://aws.amazon.com/cli/# 

- Restart terminal after installation# Add to .env as:

- Verify: `aws --version`# GEMINI_API_KEY=your_key_here

```

### Issue: AWS profile not configured

**Solution**:---

```powershell

# List current profiles## 🧪 Quick Functional Test

aws configure list-profiles

Once the terminal is running, try these commands in order:

# Configure new profile

aws configure --profile iam-user### Test 1: Help System

```

# Verify credentials> ?what is S3

aws sts get-caller-identity --profile iam-user```

```**Expected**: AI response explaining S3



### Issue: Invalid Gemini API key### Test 2: Shell Command

**Solution**:```

1. Get new key from https://makersuite.google.com/app/apikey> !echo Hello from AWS Terminal

2. Add to config.ini as:```

```ini**Expected**: "Hello from AWS Terminal" printed

[GEMINI]

api_key = your_actual_key_here### Test 3: AWS List Operation (safest test)

``````

3. Save and try again> list all S3 buckets

```

### Issue: Permission denied in AWS**Expected**: Your S3 buckets listed (or empty list if none)

**Solution**:

- Check IAM user permissions### Test 4: Command History

- Ensure user has necessary service permissions```

- Test with: `aws iam get-user --profile iam-user`Press ↑ arrow key

```

---**Expected**: Previous commands appear



## ✅ Final Checklist### Test 5: Homepage

```

Before you start using the terminal, ensure:> home

```

- [ ] Python 3.8+ installed**Expected**: ASCII art homepage redisplayed

- [ ] All dependencies installed (`pip install -r requirements.txt`)

- [ ] `config.ini` created and configured### Test 6: Clear Screen

- [ ] Gemini API key added to config.ini```

- [ ] AWS CLI installed (if using IAM/root mode)> clear

- [ ] AWS profile configured (if using IAM/root mode)```

- [ ] Terminal launches successfully**Expected**: Screen cleared

- [ ] Homepage displays correctly

### Test 7: Exit

---```

> exit

## 🚀 Next Steps```

**Expected**: Terminal exits gracefully

Once everything is verified:

---

1. **For Demo Mode**: Just run `python main.py` and start exploring

2. **For IAM Mode**: Switch with `python switch_mode.py iam` then run## 📊 System Requirements

3. **For Root Mode**: Switch with `python switch_mode.py root` then run

| Component | Minimum | Recommended |

See [QUICKSTART_AWS_PROFILES.md](../QUICKSTART_AWS_PROFILES.md) for detailed usage instructions.|-----------|---------|-------------|

| Python | 3.8 | 3.11+ |

---| RAM | 512 MB | 2 GB |

| Storage | 100 MB | 500 MB |

## 📚 Additional Resources| Internet | Required | High-speed |

| OS | Windows 10+ | Windows 11 |

- [SETUP_AWS_PROFILES.md](../SETUP_AWS_PROFILES.md) - Complete setup guide

- [QUICKSTART_AWS_PROFILES.md](../QUICKSTART_AWS_PROFILES.md) - Quick start---

- [AUTH_GUIDE.md](AUTH_GUIDE.md) - Authentication methods

- [COMMANDS.md](COMMANDS.md) - Command examples## ✅ Pre-Launch Checklist


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
