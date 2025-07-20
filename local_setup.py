#!/usr/bin/env python3
"""
Local setup script for AI Quiz Generator
Creates necessary directories and configuration files for local development
"""

import os
import sys

def create_directories():
    """Create necessary directories"""
    directories = [
        'uploads',
        'templates', 
        'static'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
           


def create_env_file():
    """Create .env file from example if it doesn't exist"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            import shutil
            shutil.copy('.env.example', '.env')

        else:
            with open('.env', 'w') as f:
                f.write("""# Google Gemini API Configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Flask Configuration  
SESSION_SECRET=your_secure_session_secret_here

# Development Settings
FLASK_ENV=development
FLASK_DEBUG=True
""")

def install_requirements():
    """Install required packages"""
    packages = [
        'flask==3.0.0',
        'flask-cors==4.0.0', 
        'google-genai==0.8.0',
        'pymupdf==1.23.14',
        'python-docx==1.1.0',
        'pydantic==2.5.2',
        'werkzeug==3.0.1'
    ]
   
    for package in packages:
        os.system(f'pip install {package}')
    


def main():
    """Main setup function"""

    
    create_directories()
    create_env_file()
    
    if '--install-deps' in sys.argv:
        install_requirements()
    

if __name__ == '__main__':
    main()