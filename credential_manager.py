"""
Credential Manager for AWS Smart Terminal
Loads credentials from AWS profiles (~/.aws/credentials) and config.ini
Supports demo, iam, and root authentication modes
"""

import configparser
import os
from pathlib import Path


class CredentialManager:
    """Manages authentication credentials using AWS profiles and config.ini"""
    
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self._load_config()
    
    def _load_config(self):
        """Load configuration from config.ini"""
        if not Path(self.config_file).exists():
            raise FileNotFoundError(
                f"Configuration file '{self.config_file}' not found!\n"
                f"Please create it from config.ini.example"
            )
        
        self.config.read(self.config_file)
    
    def get_auth_mode(self):
        """Get current authentication mode"""
        return self.config.get('AUTH', 'mode', fallback='demo')
    
    def get_gemini_api_key(self):
        """Get Gemini API key"""
        api_key = self.config.get('GEMINI', 'api_key', fallback='')
        if not api_key or api_key == 'your_gemini_api_key_here':
            raise ValueError(
                "Gemini API key not configured!\n"
                "Please add your API key to config.ini under [GEMINI] section"
            )
        return api_key
    
    def get_aws_region(self):
        """Get AWS default region"""
        return self.config.get('AWS', 'default_region', fallback='us-east-1')
    
    def get_aws_profile(self):
        """Get AWS profile name based on current mode"""
        mode = self.get_auth_mode()
        
        if mode == 'demo':
            return None
        elif mode == 'iam':
            return self.config.get('AUTH', 'iam_profile', fallback='iam-user')
        elif mode == 'root':
            return self.config.get('AUTH', 'root_profile', fallback='root-account')
        else:
            raise ValueError(f"Invalid auth mode: {mode}")
    
    def get_credentials(self):
        """
        Get all credentials as a dictionary
        Returns:
            dict: Contains auth_method, gemini_api_key, aws_profile, aws_region
        """
        mode = self.get_auth_mode()
        
        credentials = {
            'auth_method': mode,
            'gemini_api_key': self.get_gemini_api_key(),
            'aws_region': self.get_aws_region(),
            'aws_profile': self.get_aws_profile()
        }
        
        # Set AWS_PROFILE environment variable for AWS CLI
        if credentials['aws_profile']:
            os.environ['AWS_PROFILE'] = credentials['aws_profile']
            os.environ['AWS_DEFAULT_REGION'] = credentials['aws_region']
        else:
            # Remove AWS env vars in demo mode
            os.environ.pop('AWS_PROFILE', None)
        
        return credentials
    
    def is_demo_mode(self):
        """Check if running in demo mode"""
        return self.get_auth_mode() == 'demo'
    
    def get_terminal_settings(self):
        """Get terminal configuration settings"""
        return {
            'history_file': self.config.get('TERMINAL', 'history_file', fallback='.terminal_history'),
            'max_history': self.config.getint('TERMINAL', 'max_history_entries', fallback=1000)
        }


# Example usage
if __name__ == '__main__':
    try:
        cred_manager = CredentialManager()
        credentials = cred_manager.get_credentials()
        
        print("=" * 60)
        print("AWS SMART TERMINAL - CREDENTIAL STATUS")
        print("=" * 60)
        print(f"Authentication Mode: {credentials['auth_method'].upper()}")
        print(f"AWS Region: {credentials['aws_region']}")
        
        if credentials['aws_profile']:
            print(f"AWS Profile: {credentials['aws_profile']}")
            print(f"Profile Location: ~/.aws/credentials")
        else:
            print("AWS Profile: None (Demo Mode)")
        
        print(f"Gemini API Key: {'*' * 20}...{credentials['gemini_api_key'][-4:]}")
        print("=" * 60)
        
        if credentials['auth_method'] == 'demo':
            print("\n🎮 DEMO MODE ACTIVE")
            print("Commands will be previewed but not executed")
        else:
            print(f"\n✅ Ready to execute AWS commands using {credentials['auth_method'].upper()} credentials")
        
    except Exception as e:
        print(f"❌ Error: {e}")
