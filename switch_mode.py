"""
Mode Switcher for AWS Smart Terminal
Easily switch between demo, iam, and root authentication modes
"""

import sys
import configparser
from pathlib import Path


def switch_mode(mode):
    """Switch authentication mode in config.ini"""
    valid_modes = ['demo', 'iam', 'root']
    
    if mode not in valid_modes:
        print(f"❌ Invalid mode: '{mode}'")
        print(f"Valid options: {', '.join(valid_modes)}")
        return False
    
    config_file = 'config.ini'
    
    if not Path(config_file).exists():
        print(f"❌ Configuration file '{config_file}' not found!")
        print("Please create it from config.ini.example")
        return False
    
    # Read current config
    config = configparser.ConfigParser()
    config.read(config_file)
    
    # Update mode
    if 'AUTH' not in config:
        config['AUTH'] = {}
    
    old_mode = config.get('AUTH', 'mode', fallback='unknown')
    config.set('AUTH', 'mode', mode)
    
    # Write updated config
    with open(config_file, 'w') as f:
        config.write(f)
    
    # Success message
    print("=" * 60)
    print("🔄 MODE SWITCHED SUCCESSFULLY")
    print("=" * 60)
    print(f"Previous mode: {old_mode.upper()}")
    print(f"Current mode:  {mode.upper()}")
    print("=" * 60)
    
    # Mode-specific messages
    if mode == 'demo':
        print("\n🎮 DEMO MODE ACTIVE")
        print("• Commands will be previewed but NOT executed")
        print("• No AWS credentials required")
        print("• Perfect for learning and testing")
        print("\nRequirements:")
        print("✓ Gemini API key in config.ini")
    
    elif mode == 'iam':
        print("\n🔒 IAM USER MODE ACTIVE")
        print("• Commands will be executed with IAM credentials")
        print("• Recommended for production use")
        print("• Limited permissions based on IAM policy")
        print("\nRequirements:")
        print("✓ Gemini API key in config.ini")
        print("✓ AWS profile configured: aws configure --profile iam-user")
        print("\nVerify profile:")
        print("  aws sts get-caller-identity --profile iam-user")
    
    elif mode == 'root':
        print("\n⚠️  ROOT ACCOUNT MODE ACTIVE")
        print("• Commands will be executed with ROOT credentials")
        print("• NOT RECOMMENDED for production!")
        print("• Full access to all AWS services")
        print("\nRequirements:")
        print("✓ Gemini API key in config.ini")
        print("✓ AWS profile configured: aws configure --profile root-account")
        print("\nVerify profile:")
        print("  aws sts get-caller-identity --profile root-account")
    
    print("\n💡 Start terminal: python main.py")
    
    return True


def show_current_mode():
    """Display current authentication mode"""
    config_file = 'config.ini'
    
    if not Path(config_file).exists():
        print(f"❌ Configuration file '{config_file}' not found!")
        return
    
    config = configparser.ConfigParser()
    config.read(config_file)
    
    current_mode = config.get('AUTH', 'mode', fallback='unknown')
    
    print("=" * 60)
    print("CURRENT AUTHENTICATION MODE")
    print("=" * 60)
    print(f"Mode: {current_mode.upper()}")
    
    if current_mode == 'iam':
        profile = config.get('AUTH', 'iam_profile', fallback='iam-user')
        print(f"Profile: {profile}")
    elif current_mode == 'root':
        profile = config.get('AUTH', 'root_profile', fallback='root-account')
        print(f"Profile: {profile}")
    
    print("=" * 60)


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("AWS Smart Terminal - Mode Switcher")
        print("=" * 60)
        print("\nUsage:")
        print("  python switch_mode.py <mode>")
        print("  python switch_mode.py status")
        print("\nAvailable modes:")
        print("  demo   - Preview commands without execution (no AWS account needed)")
        print("  iam    - Execute with IAM user credentials (recommended)")
        print("  root   - Execute with root account credentials (not recommended)")
        print("\nExamples:")
        print("  python switch_mode.py demo")
        print("  python switch_mode.py iam")
        print("  python switch_mode.py status")
        print("\n" + "=" * 60)
        show_current_mode()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'status':
        show_current_mode()
    elif command in ['demo', 'iam', 'root']:
        switch_mode(command)
    else:
        print(f"❌ Unknown command: '{command}'")
        print("Valid commands: demo, iam, root, status")


if __name__ == '__main__':
    main()
