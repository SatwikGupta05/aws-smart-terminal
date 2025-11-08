"""
Secure .env File Manager
Encrypts and decrypts .env file with password protection
"""

import os
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import getpass


def derive_key(password: str, salt: bytes) -> bytes:
    """Derive encryption key from password"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_env_file(password: str):
    """Encrypt .env file"""
    env_path = ".env"
    encrypted_path = ".env.encrypted"
    salt_path = ".env.salt"
    
    if not os.path.exists(env_path):
        print("❌ .env file not found!")
        return False
    
    # Generate salt
    salt = os.urandom(16)
    
    # Derive key from password
    key = derive_key(password, salt)
    fernet = Fernet(key)
    
    # Read and encrypt .env file
    with open(env_path, 'rb') as f:
        data = f.read()
    
    encrypted_data = fernet.encrypt(data)
    
    # Save encrypted file and salt
    with open(encrypted_path, 'wb') as f:
        f.write(encrypted_data)
    
    with open(salt_path, 'wb') as f:
        f.write(salt)
    
    # Delete original .env file
    os.remove(env_path)
    
    print("✅ .env file encrypted successfully!")
    print(f"📁 Encrypted file: {encrypted_path}")
    print(f"🔑 Salt file: {salt_path}")
    print("\n⚠️  Keep these files safe. You'll need the password to decrypt!")
    return True


def decrypt_env_file(password: str):
    """Decrypt .env file"""
    encrypted_path = ".env.encrypted"
    salt_path = ".env.salt"
    env_path = ".env"
    
    if not os.path.exists(encrypted_path):
        print("❌ .env.encrypted file not found!")
        return False
    
    if not os.path.exists(salt_path):
        print("❌ .env.salt file not found!")
        return False
    
    # Read salt
    with open(salt_path, 'rb') as f:
        salt = f.read()
    
    # Derive key from password
    key = derive_key(password, salt)
    fernet = Fernet(key)
    
    # Read and decrypt
    try:
        with open(encrypted_path, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Save decrypted .env file
        with open(env_path, 'wb') as f:
            f.write(decrypted_data)
        
        print("✅ .env file decrypted successfully!")
        print(f"📁 Decrypted file: {env_path}")
        return True
        
    except Exception as e:
        print(f"❌ Decryption failed! Wrong password or corrupted file.")
        print(f"   Error: {str(e)}")
        return False


def lock_env():
    """Encrypt .env file (lock it)"""
    print("\n🔒 Locking .env file...")
    print("=" * 50)
    password = getpass.getpass("Enter password to encrypt .env: ")
    confirm = getpass.getpass("Confirm password: ")
    
    if password != confirm:
        print("❌ Passwords don't match!")
        return
    
    if len(password) < 8:
        print("❌ Password must be at least 8 characters!")
        return
    
    encrypt_env_file(password)


def unlock_env():
    """Decrypt .env file (unlock it)"""
    print("\n🔓 Unlocking .env file...")
    print("=" * 50)
    password = getpass.getpass("Enter password to decrypt .env: ")
    
    decrypt_env_file(password)


def main():
    """Main function"""
    print("\n" + "=" * 50)
    print("🔐 Secure .env File Manager")
    print("=" * 50)
    
    if os.path.exists(".env"):
        print("\n📄 Status: .env file is UNLOCKED (plaintext)")
        print("\n1. Lock .env file (encrypt)")
        print("2. Exit")
        choice = input("\nChoice (1-2): ").strip()
        
        if choice == "1":
            lock_env()
        else:
            print("👋 Exiting...")
    
    elif os.path.exists(".env.encrypted"):
        print("\n🔒 Status: .env file is LOCKED (encrypted)")
        print("\n1. Unlock .env file (decrypt)")
        print("2. Exit")
        choice = input("\nChoice (1-2): ").strip()
        
        if choice == "1":
            unlock_env()
        else:
            print("👋 Exiting...")
    
    else:
        print("\n❌ No .env or .env.encrypted file found!")
        print("   Create a .env file first, then run this script to encrypt it.")


if __name__ == "__main__":
    main()
