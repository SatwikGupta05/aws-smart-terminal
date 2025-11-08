# 🔐 Secure .env File Protection

## Overview

The `secure_env.py` script provides password-based encryption for your `.env` file to protect sensitive AWS credentials and API keys.

## Why Use This?

Your `.env` file contains:
- AWS Access Keys
- AWS Secret Keys
- Gemini API Keys
- Other sensitive credentials

**Without encryption**, anyone with access to your computer can read these credentials in plaintext.

**With encryption**, the credentials are encrypted and require a password to access.

---

## Installation

Install the required cryptography library:

```powershell
pip install cryptography
```

Or install all requirements:

```powershell
pip install -r requirements.txt
```

---

## Usage

### 🔒 Locking (Encrypting) Your .env File

**When to use:** Before committing to Git, sharing your project, or when leaving your computer unattended.

```powershell
python secure_env.py
```

**What happens:**
1. Prompts for a password (minimum 8 characters)
2. Encrypts your `.env` file
3. Creates:
   - `.env.encrypted` - Encrypted credentials
   - `.env.salt` - Encryption salt
4. Deletes the plaintext `.env` file

**Output:**
```
✅ .env file encrypted successfully!
📁 Encrypted file: .env.encrypted
🔑 Salt file: .env.salt

⚠️  Keep these files safe. You'll need the password to decrypt!
```

---

### 🔓 Unlocking (Decrypting) Your .env File

**When to use:** Before running the AWS terminal or when you need to edit credentials.

```powershell
python secure_env.py
```

**What happens:**
1. Prompts for password
2. Decrypts `.env.encrypted` using your password
3. Creates `.env` file with plaintext credentials
4. Ready to use!

**Output:**
```
✅ .env file decrypted successfully!
📁 Decrypted file: .env
```

---

## Workflow Example

### Initial Setup
```powershell
# 1. Create your .env file with credentials
notepad .env

# 2. Lock it with password
python secure_env.py
# Choose option 1: Lock .env file
# Enter password: ********
```

### Daily Usage
```powershell
# 1. Unlock to use terminal
python secure_env.py
# Choose option 1: Unlock .env file
# Enter password: ********

# 2. Use the terminal
python main.py

# 3. Lock it again when done
python secure_env.py
# Choose option 1: Lock .env file
```

---

## Security Features

✅ **Password-based encryption** using PBKDF2 (100,000 iterations)
✅ **Strong encryption** using Fernet (AES-128 CBC)
✅ **Unique salt** for each encryption
✅ **No password storage** - password never saved to disk
✅ **Git protection** - `.env.encrypted` and `.env.salt` in `.gitignore`

---

## Important Notes

### ⚠️ Password Security
- **Use a strong password** (minimum 8 characters, but longer is better)
- **Don't forget your password** - there's no recovery method!
- **Don't share your password** - it protects all your credentials

### ⚠️ File Safety
- Keep both `.env.encrypted` and `.env.salt` files
- Both files are needed to decrypt
- Backup these files in a secure location

### ⚠️ Git Protection
- The plaintext `.env` is in `.gitignore` (never committed)
- The encrypted files are also in `.gitignore` (extra safety)
- Always verify before pushing to Git!

---

## Troubleshooting

### "Wrong password or corrupted file"
- **Solution:** Try entering password again carefully
- **Cause:** Wrong password or files were modified

### "No .env or .env.encrypted file found"
- **Solution:** Create `.env` file first with your credentials
- Use `.env.example` as a template

### "Passwords don't match"
- **Solution:** Type carefully, passwords must match when encrypting

---

## Quick Commands

**Encrypt .env:**
```powershell
python secure_env.py
# Choose 1
```

**Decrypt .env:**
```powershell
python secure_env.py
# Choose 1
```

**Install dependencies:**
```powershell
pip install cryptography
```

---

## What Gets Protected?

Everything in your `.env` file:
```env
AWS_AUTH_METHOD=iam
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE    # ← Protected
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI...     # ← Protected
AWS_DEFAULT_REGION=us-east-1
GEMINI_API_KEY=AIzaSyC_...                 # ← Protected
```

---

## Best Practices

1. **Lock when not in use** - Encrypt `.env` when you're done working
2. **Strong passwords** - Use 12+ characters with mix of letters, numbers, symbols
3. **Backup encrypted files** - Keep `.env.encrypted` and `.env.salt` backed up
4. **Don't commit .env** - Always keep `.env` in `.gitignore`
5. **Rotate credentials** - If password is compromised, change AWS keys immediately

---

## Alternative: Manual Encryption

If you prefer, you can manually encrypt/decrypt:

**Encrypt:**
```powershell
python -c "from secure_env import encrypt_env_file; encrypt_env_file(input('Password: '))"
```

**Decrypt:**
```powershell
python -c "from secure_env import decrypt_env_file; decrypt_env_file(input('Password: '))"
```

---

**Stay secure! 🔐**
