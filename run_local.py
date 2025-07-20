#!/usr/bin/env python3
"""
Local development server for AI Quiz Generator
Run this file to start the application locally
"""

import os
import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def load_env_file():
    """Load environment variables from .env file"""
    env_file = current_dir / '.env'
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
        


def check_requirements():
    """Check if required packages are installed"""
    required_packages = [
        'flask',
        'flask_cors', 
        'google.genai',
        'fitz',  # PyMuPDF
        'docx',  # python-docx
        'pydantic'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == 'google.genai':
                import google.genai
            elif package == 'fitz':
                import fitz
            elif package == 'docx':
                import docx
            elif package == 'flask_cors':
                import flask_cors
            else:
                __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:

        return False
    
    return True

def main():
    """Main function to start the local server"""

    
    # Load environment variables
    load_env_file()
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check for API key
    if not os.environ.get('GEMINI_API_KEY'):
      
        sys.exit(1)
    
    # Import and run the Flask app
    try:
        from app import app

        
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            use_reloader=True
        )
    except Exception as e:
       
        sys.exit(1)

if __name__ == '__main__':
    main()