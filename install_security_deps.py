#!/usr/bin/env python3
"""
Install security dependencies for the Account Service
"""
import subprocess
import sys

def install_dependencies():
    """Install the new security dependencies"""
    print("Installing security dependencies...")
    
    dependencies = [
        "Flask-Talisman==1.0.0",
        "Flask-CORS==4.0.0",
        "requests==2.31.0"
    ]
    
    for dep in dependencies:
        print(f"Installing {dep}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✓ {dep} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install {dep}: {e}")
            return False
    
    print("\nAll security dependencies installed successfully!")
    return True

def main():
    """Main function"""
    print("Account Service Security Dependencies Installer")
    print("=" * 50)
    print()
    
    if install_dependencies():
        print("\nNext steps:")
        print("1. Copy env.template to .env and configure your settings")
        print("2. Start your Flask service")
        print("3. Run test_security.py to verify the implementation")
        print("\nFor more information, see SECURITY.md")
    else:
        print("\nInstallation failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 